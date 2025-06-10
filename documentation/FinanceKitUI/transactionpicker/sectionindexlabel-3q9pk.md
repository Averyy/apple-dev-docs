# sectionIndexLabel(_:)

**Framework**: FinanceKitUI  
**Kind**: method

Sets the title that is used for the section index label pointing to this section, typically only a single character long.

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
nonisolated
func sectionIndexLabel<S>(_ label: S?) -> some View where S : StringProtocol
```

#### Discussion

- See also `listSectionIndexVisibility(_:)`

## Parameters

- `title`: The title to use for the index label for this   section, or   to display no label for this section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekitui/transactionpicker/sectionindexlabel(_:)-3q9pk)*