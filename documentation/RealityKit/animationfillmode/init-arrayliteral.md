# init(arrayLiteral:)

**Framework**: RealityKit  
**Kind**: init

Creates a set containing the elements of the given array literal.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

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

- [init()](animationfillmode/init.md)
  Creates an empty option set.
- [init<S>(S)](animationfillmode/init(_:).md)
  Creates a new set from a finite sequence of items.
- [init(rawValue: Int8)](animationfillmode/init(rawvalue:).md)
  Creates a fill mode from its backing data type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationfillmode/init(arrayliteral:))*