# rawValue

**Framework**: App Intents  
**Kind**: property

The corresponding value of the raw type.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
var rawValue: String { get }
```

#### Discussion

A new instance initialized with `rawValue` will be equivalent to this instance. For example:

```swift
enum PaperSize: String {
    case A4, A5, Letter, Legal
}

let selectedSize = PaperSize.Letter
print(selectedSize.rawValue)
// Prints "Letter"

print(selectedSize == PaperSize(rawValue: selectedSize.rawValue)!)
// Prints "true"
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentperson/parametermode/rawvalue-swift.property)*