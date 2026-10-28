# init(_:destination:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a control, consisting of a URL and a title string, used to navigate to a URL.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
nonisolated
init<S>(_ title: S, destination: URL) where S : StringProtocol
```

Available when `Label` is `Text`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, destination: URL)
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, destination: URL)
```

## Discussion

Use [`Link`](../link.md) to create a control that your app uses to navigate to a URL that you provide. The example below creates a link to `example.com` and displays the title string you provide as a link-styled view in your app:

```swift
func marketingLink(_ callToAction: String) -> Link {
    Link(callToAction,
        destination: URL(string: "https://www.example.com/")!)
}
```

## Parameters

- `title`: A text string used as the title for describing the underlying `destination` URL.
- `destination`: The URL for the link.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/link/init(_:destination:)-5es0x)*