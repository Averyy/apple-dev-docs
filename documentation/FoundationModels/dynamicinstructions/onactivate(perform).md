# onActivate(perform:)

**Framework**: Foundation Models  
**Kind**: method  
**Role**: Instance Method

Runs an action when these dynamic instructions become active.

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
func onActivate(perform action: sending @escaping @isolated(any) () async -> Void) -> some DynamicInstructions
```

## Discussion

Dynamic instructions become active when they are first included in the session’s resolved configuration, or when they are re-included after being absent. Use this to set up state tied to the instructions’ lifecycle:

```swift
struct MyInstructions: DynamicInstructions {
  var body: some DynamicInstructions {
    Instructions("You are a helpful assistant.")
      .onActivate {
        activeInstructions = "assistant"
      }
  }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/dynamicinstructions/onactivate(perform:))*