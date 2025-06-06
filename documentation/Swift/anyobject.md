# AnyObject

**Framework**: Swift  
**Kind**: typealias

The protocol to which all classes implicitly conform.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
typealias AnyObject
```

#### Discussion

You use `AnyObject` when you need the flexibility of an untyped object or when you use bridged Objective-C methods and properties that return an untyped result. `AnyObject` can be used as the concrete type for an instance of any class, class type, or class-only protocol. For example:

```swift
class FloatRef {
    let value: Float
    init(_ value: Float) {
        self.value = value
    }
}

let x = FloatRef(2.3)
let y: AnyObject = x
let z: AnyObject = FloatRef.self
```

`AnyObject` can also be used as the concrete type for an instance of a type that bridges to an Objective-C class. Many value types in Swift bridge to Objective-C counterparts, like `String` and `Int`.

```swift
let s: AnyObject = "This is a bridged string." as NSString
print(s is NSString)
// Prints "true"

let v: AnyObject = 100 as NSNumber
print(type(of: v))
// Prints "__NSCFNumber"
```

The flexible behavior of the `AnyObject` protocol is similar to Objective-C’s `id` type. For this reason, imported Objective-C types frequently use `AnyObject` as the type for properties, method parameters, and return values.

### Casting Anyobject Instances to a Known Type

Objects with a concrete type of `AnyObject` maintain a specific dynamic type and can be cast to that type using one of the type-cast operators (`as`, `as?`, or `as!`).

This example uses the conditional downcast operator (`as?`) to conditionally cast the `s` constant declared above to an instance of Swift’s `String` type.

```swift
if let message = s as? String {
    print("Successful cast to String: \(message)")
}
// Prints "Successful cast to String: This is a bridged string."
```

If you have prior knowledge that an `AnyObject` instance has a particular type, you can use the unconditional downcast operator (`as!`). Performing an invalid cast triggers a runtime error.

```swift
let message = s as! String
print("Successful cast to String: \(message)")
// Prints "Successful cast to String: This is a bridged string."

let badCase = v as! String
// Runtime error
```

Casting is always safe in the context of a `switch` statement.

```swift
let mixedArray: [AnyObject] = [s, v]
for object in mixedArray {
    switch object {
    case let x as String:
        print("'\(x)' is a String")
    default:
        print("'\(object)' is not a String")
    }
}
// Prints "'This is a bridged string.' is a String"
// Prints "'100' is not a String"
```

### Accessing Objective C Methods and Properties

When you use `AnyObject` as a concrete type, you have at your disposal every `@objc` method and property—that is, methods and properties imported from Objective-C or marked with the `@objc` attribute. Because Swift can’t guarantee at compile time that these methods and properties are actually available on an `AnyObject` instance’s underlying type, these `@objc` symbols are available as implicitly unwrapped optional methods and properties, respectively.

This example defines an `IntegerRef` type with an `@objc` method named `getIntegerValue()`.

```swift
class IntegerRef {
    let value: Int
    init(_ value: Int) {
        self.value = value
    }

    @objc func getIntegerValue() -> Int {
        return value
    }
}

func getObject() -> AnyObject {
    return IntegerRef(100)
}

let obj: AnyObject = getObject()
```

In the example, `obj` has a static type of `AnyObject` and a dynamic type of `IntegerRef`. You can use optional chaining to call the `@objc` method `getIntegerValue()` on `obj` safely. If you’re sure of the dynamic type of `obj`, you can call `getIntegerValue()` directly.

```swift
let possibleValue = obj.getIntegerValue?()
print(possibleValue)
// Prints "Optional(100)"

let certainValue = obj.getIntegerValue()
print(certainValue)
// Prints "100"
```

If the dynamic type of `obj` doesn’t implement a `getIntegerValue()` method, the system returns a runtime error when you initialize `certainValue`.

Alternatively, if you need to test whether `obj.getIntegerValue()` exists, use optional binding before calling the method.

```swift
if let f = obj.getIntegerValue {
    print("The value of 'obj' is \(f())")
} else {
    print("'obj' does not have a 'getIntegerValue()' method")
}
// Prints "The value of 'obj' is 100"
```

## See Also

- [typealias AnyClass](anyclass.md)
  The protocol to which all class types implicitly conform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/anyobject)*