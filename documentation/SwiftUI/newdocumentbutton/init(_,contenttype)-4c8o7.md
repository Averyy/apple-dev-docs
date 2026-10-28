# init(_:contentType:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates and opens new documents.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
nonisolated
init(_ title: LocalizedStringKey, contentType: UTType? = nil)
```

Available when `Label` is `Text`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ title: LocalizedStringResource, contentType: UTType? = nil)
```

```swift
nonisolated
init(_ label: Text? = nil, contentType: UTType? = nil)
```

```swift
nonisolated
init(_ title: some StringProtocol, contentType: UTType? = nil)
```

## Parameters

- `title`: A title key to use as the button title.
- `contentType`: An optional content type of the document to create.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/newdocumentbutton/init(_:contenttype:)-4c8o7)*