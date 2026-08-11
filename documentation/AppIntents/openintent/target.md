# target

**Framework**: App Intents  
**Kind**: property  
**Required**: Yes

The item to open in your app.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
var target: Self.Value { get set }
```

#### Discussion

Set this property to a dynamic or static type your app defines, such as an [`AppEntity`](appentity.md) or [`AppEnum`](appenum.md). Use this value to determine what content to show in your app’s interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/openintent/target)*