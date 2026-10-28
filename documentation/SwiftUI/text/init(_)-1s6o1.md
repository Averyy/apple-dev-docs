# init(_:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a text view that displays a localized string resource.

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
init(_ resource: LocalizedStringResource)
```

**Other overloads**:

```swift
init(_ attributedContent: AttributedString)
```

```swift
init(_ dates: ClosedRange<Date>)
```

```swift
init(_ image: Image)
```

```swift
init(_ interval: DateInterval)
```

```swift
init<S>(_ content: S) where S : StringProtocol
```

## Discussion

Use this initializer to display a localized string that is represented by a [`LocalizedStringResource`](../../Foundation/localizedstringresource.md)

```swift
var object = LocalizedStringResource("pencil")
Text(object) // Localizes the resource if possible, or displays "pencil" if not.
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/init(_:)-1s6o1)*