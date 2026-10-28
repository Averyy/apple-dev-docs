# init(_:destination:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a control, consisting of a URL and a title key, used to navigate to a URL.

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
init(_ titleKey: LocalizedStringKey, destination: URL)
```

Available when `Label` is `Text`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, destination: URL)
```

```swift
nonisolated
init<S>(_ title: S, destination: URL) where S : StringProtocol
```

## Discussion

Use [`Link`](../link.md) to create a control that your app uses to navigate to a URL that you provide. The example below creates a link to `example.com` and uses `Visit Example Co` as the title key to generate a link-styled view in your app:

```swift
Link("Visit Example Co",
      destination: URL(string: "https://www.example.com/")!)
```

## Parameters

- `titleKey`: The key for the localized title that describes the purpose of this link.
- `destination`: The URL for the link.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/link/init(_:destination:)-3sq22)*