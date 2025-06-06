# type(of:)

**Framework**: Swift  
**Kind**: func

Returns the dynamic type of a value.

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
func type<T, Metatype>(of value: T) -> Metatype
```

#### Return Value

The dynamic type, which is a metatype instance.

#### Discussion

You can use the `type(of:)` function to find the dynamic type of a value, particularly when the dynamic type is different from the static type. The  of a value is the known, compile-time type of the value. The  of a value is the value’s actual type at run-time, which can be a subtype of its concrete type.

In the following code, the `count` variable has the same static and dynamic type: `Int`. When `count` is passed to the `printInfo(_:)` function, however, the `value` parameter has a static type of `Any` (the type declared for the parameter) and a dynamic type of `Int`.

```swift
func printInfo(_ value: Any) {
    let t = type(of: value)
    print("'\(value)' of type '\(t)'")
}

let count: Int = 5
printInfo(count)
// '5' of type 'Int'
```

The dynamic type returned from `type(of:)` is a  (`T.Type`) for a class, structure, enumeration, or other nonprotocol type `T`, or an  (`P.Type`) for a protocol or protocol composition `P`. When the static type of the value passed to `type(of:)` is constrained to a class or protocol, you can use that metatype to access initializers or other static members of the class or protocol.

For example, the parameter passed as `value` to the `printSmileyInfo(_:)` function in the example below is an instance of the `Smiley` class or one of its subclasses. The function uses `type(of:)` to find the dynamic type of `value`, which itself is an instance of the `Smiley.Type` metatype.

```swift
class Smiley {
    class var text: String {
        return ":)"
    }
}

class EmojiSmiley: Smiley {
     override class var text: String {
        return "😀"
    }
}

func printSmileyInfo(_ value: Smiley) {
    let smileyType = type(of: value)
    print("Smile!", smileyType.text)
}

let emojiSmiley = EmojiSmiley()
printSmileyInfo(emojiSmiley)
// Smile! 😀
```

In this example, accessing the `text` property of the `smileyType` metatype retrieves the overridden value from the `EmojiSmiley` subclass, instead of the `Smiley` class’s original definition.

### Finding the Dynamic Type in a Generic Context

Normally, you don’t need to be aware of the difference between concrete and existential metatypes, but calling `type(of:)` can yield unexpected results in a generic context with a type parameter bound to a protocol. In a case like this, where a generic parameter `T` is bound to a protocol `P`, the type parameter is not statically known to be a protocol type in the body of the generic function. As a result, `type(of:)` can only produce the concrete metatype `P.Protocol`.

The following example defines a `printGenericInfo(_:)` function that takes a generic parameter and declares the `String` type’s conformance to a new protocol `P`. When `printGenericInfo(_:)` is called with a string that has `P` as its static type, the call to `type(of:)` returns `P.self` instead of `String.self` (the dynamic type inside the parameter).

```swift
func printGenericInfo<T>(_ value: T) {
    let t = type(of: value)
    print("'\(value)' of type '\(t)'")
}

protocol P {}
extension String: P {}

let stringAsP: P = "Hello!"
printGenericInfo(stringAsP)
// 'Hello!' of type 'P'
```

This unexpected result occurs because the call to `type(of: value)` inside `printGenericInfo(_:)` must return a metatype that is an instance of `T.Type`, but `String.self` (the expected dynamic type) is not an instance of `P.Type` (the concrete metatype of `value`). To get the dynamic type inside `value` in this generic context, cast the parameter to `Any` when calling `type(of:)`.

```swift
func betterPrintGenericInfo<T>(_ value: T) {
    let t = type(of: value as Any)
    print("'\(value)' of type '\(t)'")
}

betterPrintGenericInfo(stringAsP)
// 'Hello!' of type 'String'
```

## Parameters

- `value`: The value for which to find the dynamic type.

## See Also

- [struct Mirror](mirror.md)
  A representation of the substructure and display style of an instance of any type.
- [struct ObjectIdentifier](objectidentifier.md)
  A unique identifier for a class instance or metatype.
- [func == ((any Any.Type)?, (any Any.Type)?) -> Bool](==(_:_:)-w1qf.md)
  Returns a Boolean value indicating whether two types are identical.
- [func != ((any Any.Type)?, (any Any.Type)?) -> Bool](!=(_:_:)-6s4z0.md)
  Returns a Boolean value indicating whether two types are not identical.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/type(of:))*