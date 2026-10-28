# init(_:_:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Create a slider tick with a label from a string title.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
init<S>(_ title: S, _ value: V) where S : StringProtocol
```

Available when `V` conforms to `BinaryFloatingPoint`.

**Other overloads**:

```swift
init(_ titleKey: LocalizedStringKey, _ value: V)
```

```swift
init(_ titleResource: LocalizedStringResource, _ value: V)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/slidertick/init(_:_:)-8gr0n)*