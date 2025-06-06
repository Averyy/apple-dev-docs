# rawValue

**Framework**: Create ML  
**Kind**: property

The corresponding value of the raw type.

**Availability**:
- macOS 11.0+

## Declaration

```swift
let rawValue: Int
```

#### Discussion

A new instance initialized with `rawValue` will be equivalent to this instance. For example:

```None
enum PaperSize: String {
    case A4, A5, Letter, Legal
}

let selectedSize = PaperSize.Letter
print(selectedSize.rawValue)
// Prints "Letter"

print(selectedSize == PaperSize(rawValue: selectedSize.rawValue)!)
// Prints "true"
```

## See Also

- [var isEmpty: Bool](mlactionclassifier/videoaugmentationoptions/isempty.md)
  A Boolean value that indicates whether the set has no elements.
- [func contains(Self) -> Bool](mlactionclassifier/videoaugmentationoptions/contains(_:).md)
  Returns a Boolean value that indicates whether a given element is a member of the option set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactionclassifier/videoaugmentationoptions/rawvalue-swift.property)*