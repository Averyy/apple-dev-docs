# init(arrayLiteral:)

**Framework**: RealityKit  
**Kind**: init

Creates a set containing the elements of the given array literal.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+

## Declaration

```swift
init(arrayLiteral: Self.Element...)
```

#### Discussion

Do not call this initializer directly. It is used by the compiler when you use an array literal. Instead, create a new set using an array literal as its value by enclosing a comma-separated list of values in square brackets. You can use an array literal anywhere a set is expected by the type context.

Here, a set of strings is created from an array literal holding only strings:

```None
let ingredients: Set = ["cocoa beans", "sugar", "cocoa butter", "salt"]
if ingredients.isSuperset(of: ["sugar", "salt"]) {
    print("Whatever it is, it's bound to be delicious!")
}
// Prints "Whatever it is, it's bound to be delicious!"
```

## Parameters

- `arrayLiteral`: A list of elements of the new set.

## See Also

- [init()](arview/entitygestures/init.md)
  Creates an empty option set.
- [init<S>(S)](arview/entitygestures/init(_:).md)
  Creates a new set from a finite sequence of items.
- [ARView.EntityGestures.Element](arview/entitygestures/element.md)
  The element type of the option set.
- [ARView.EntityGestures.ArrayLiteralElement](arview/entitygestures/arrayliteralelement.md)
  The type of the elements of an array literal.
- [init(rawValue: Int)](arview/entitygestures/init(rawvalue:).md)
  Creates a new option set from the given raw value.
- [let rawValue: Int](arview/entitygestures/rawvalue-swift.property.md)
  The corresponding value of the raw type.
- [ARView.EntityGestures.RawValue](arview/entitygestures/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/entitygestures/init(arrayliteral:))*