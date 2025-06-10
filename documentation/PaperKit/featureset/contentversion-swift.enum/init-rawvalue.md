# init(rawValue:)

**Framework**: PaperKit  
**Kind**: init

Creates a new instance with the specified raw value.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
init?(rawValue: Int)
```

#### Discussion

If there is no value of the type that corresponds with the specified raw value, this initializer returns `nil`. For example:

```None
enum PaperSize: String {
    case A4, A5, Letter, Legal
}

print(PaperSize(rawValue: "Legal"))
// Prints "Optional(PaperSize.Legal)"

print(PaperSize(rawValue: "Tabloid"))
// Prints "nil"
```

## Parameters

- `rawValue`: The raw value to use for the new instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/featureset/contentversion-swift.enum/init(rawvalue:))*