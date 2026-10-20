# init(_:destination:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a control, consisting of a URL and a title resource, used to navigate to a URL.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, destination: URL)
```

Available when `Label` is `Text`.

**Other overloads**:

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, destination: URL)
```

```swift
nonisolated
init<S>(_ title: S, destination: URL) where S : StringProtocol
```

#### Discussion

Use [`Link`](../link.md) to create a control that your app uses to navigate to a URL that you provide. The example below creates a link to `example.com` and uses `Visit Example Co` as the title key to generate a link-styled view in your app:

```swift
Link("Visit Example Co",
      destination: URL(string: "https://www.example.com/")!)
```

## Parameters

- `titleResource`: The localized title that describes the purpose of this link.
- `destination`: The URL for the link.

## See Also

### Creating a link
- [init(destination: URL, label: () -> Label)](./init%28destination,label%29.md)
  Creates a control, consisting of a URL and a label, used to navigate to the given URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/link/init(_:destination:))*