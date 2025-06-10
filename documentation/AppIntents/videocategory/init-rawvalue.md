# init(rawValue:)

**Framework**: App Intents  
**Kind**: init

Creates a new instance with the specified raw value.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst ?+
- macOS 14.2+
- tvOS 17.2+
- visionOS ?+

## Declaration

```swift
init?(rawValue: String)
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

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/videocategory/init(rawvalue:))*