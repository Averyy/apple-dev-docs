# wrappedValue

**Framework**: SwiftUI  
**Kind**: property

The current value of the environment property.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var wrappedValue: Value { get }
```

#### Discussion

The wrapped value property provides primary access to the value’s data. However, you don’t access `wrappedValue` directly. Instead, you read the property variable created with the [`Environment`](environment.md) property wrapper:

```swift
@Environment(\.colorScheme) var colorScheme: ColorScheme

var body: some View {
    if colorScheme == .dark {
        DarkContent()
    } else {
        LightContent()
    }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environment/wrappedvalue)*