# popPanel(completion:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Pops the top panel from the overlay’s panel stack.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
func popPanel(completion: ((Bool, (any Error)?) -> Void)? = nil)
```

```swift
func popPanel() async throws -> Bool
```

```objc
- (void) popPanelWithCompletion:(void (^)(BOOL success, NSError *error)) completion;
```

## Parameters

- `completion`: An optional block called when the panel has been popped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplate/poppanel(completion:))*