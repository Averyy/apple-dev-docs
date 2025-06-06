# applied(to:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Extracts human body poses from a pixel buffer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func applied(to image: CIImage, eventHandler: EventHandler? = nil) async throws -> [Pose]
```

#### Return Value

A array of  poses from all detected persons.

## Parameters

- `image`: An image.
- `eventHandler`: An event handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/humanbodyposeextractor/applied(to:eventhandler:))*