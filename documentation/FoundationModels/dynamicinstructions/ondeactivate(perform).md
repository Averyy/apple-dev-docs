# onDeactivate(perform:)

**Framework**: Foundation Models  
**Kind**: method  
**Role**: Instance Method

Runs an action when these dynamic instructions become inactive.

**Availability**:
- iOS 27.2+
- iPadOS 27.2+
- Mac Catalyst 27.2+
- macOS 27.2+
- tvOS 27.2+
- visionOS 27.2+
- watchOS 27.2+

## Declaration

```swift
func onDeactivate(perform action: sending @escaping @isolated(any) () async -> Void) -> some DynamicInstructions
```

## Discussion

Dynamic instructions become inactive when they are no longer included in the session’s resolved configuration after previously being active. Use this to tear down state tied to the instructions’ lifecycle:

```swift
struct MyInstructions: DynamicInstructions {
  var body: some DynamicInstructions {
    Instructions("You are a helpful assistant.")
      .onDeactivate {
        activeInstructions = nil
      }
  }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/dynamicinstructions/ondeactivate(perform:))*