# rawValue

**Framework**: Create ML Components  
**Kind**: property

The corresponding value of the raw type.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var rawValue: String
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

- [static let root: JointKey](jointkey/root.md)
  A key associated with root joint in a body pose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/jointkey/rawvalue-swift.property)*