# init(rawValue:)

**Framework**: Swift  
**Kind**: init

Creates a new instance with the specified raw value.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
init?(rawValue: UInt8)
```

#### Discussion

If there is no value of the type that corresponds with the specified raw value, this initializer returns `nil`. For example:

```swift
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

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unicode/utf8/validationerror/kind-swift.struct/init(rawvalue:))*