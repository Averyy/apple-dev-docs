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

## See Also

### Displaying overlay panels
- [func showPanel(CPMapPanel, completion: ((Bool, (any Error)?) -> Void)?)](./showpanel%28_,completion%29.md)
  Shows an overlay with the specified panel.
- [func hidePanel(completion: ((Bool, (any Error)?) -> Void)?)](./hidepanel%28completion%29.md)
  Hides the overlay.
- [func pushPanel(CPMapPanel, completion: ((Bool, (any Error)?) -> Void)?)](./pushpanel%28_,completion%29.md)
  Pushes a new panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplate/poppanel(completion:))*