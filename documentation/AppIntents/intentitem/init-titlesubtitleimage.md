# init(_:title:subtitle:image:)

**Framework**: App Intents  
**Kind**: init

Creates an item with the specified value and visual attributes.

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
init(_ value: Value, title: LocalizedStringResource, subtitle: LocalizedStringResource? = nil, image: DisplayRepresentation.Image? = nil)
```

#### Discussion

> **Note**: The system uses the provided values even when `value` conforms to the [`DisplayRepresentable`](displayrepresentable.md) protocol.

## Parameters

- `value`: The value the item represents.
- `title`: The item’s title.
- `subtitle`: The item’s subtitle.
- `image`: An image to display alongside the item’s title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentitem/init(_:title:subtitle:image:))*