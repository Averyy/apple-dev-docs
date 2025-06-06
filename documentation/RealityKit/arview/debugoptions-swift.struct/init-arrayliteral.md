# init(arrayLiteral:)

**Framework**: RealityKit  
**Kind**: init

Creates a set containing the elements of the given array literal.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+

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

- [init()](arview/debugoptions-swift.struct/init.md)
  Creates an empty option set.
- [init<S>(S)](arview/debugoptions-swift.struct/init(_:).md)
  Creates a new set from a finite sequence of items.
- [ARView.DebugOptions.Element](arview/debugoptions-swift.struct/element.md)
  The element type of the option set.
- [ARView.DebugOptions.ArrayLiteralElement](arview/debugoptions-swift.struct/arrayliteralelement.md)
  The type of the elements of an array literal.
- [init(rawValue: Int)](arview/debugoptions-swift.struct/init(rawvalue:).md)
  Create a debug options enumeration from a raw value.
- [let rawValue: Int](arview/debugoptions-swift.struct/rawvalue-swift.property.md)
  Options for drawing overlay content in a scene that aids in debugging the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/debugoptions-swift.struct/init(arrayliteral:))*