# hidePanel(completion:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Hides the overlay.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
func hidePanel(completion: ((Bool, (any Error)?) -> Void)? = nil)
```

```swift
func hidePanel() async throws -> Bool
```

```objc
- (void) hidePanelWithCompletion:(void (^)(BOOL success, NSError *error)) completion;
```

## Parameters

- `completion`: An optional block called when the overlay has been hidden.

## See Also

### Displaying overlay panels
- [func showPanel(CPMapPanel, completion: ((Bool, (any Error)?) -> Void)?)](./showpanel%28_,completion%29.md)
  Shows an overlay with the specified panel.
- [func pushPanel(CPMapPanel, completion: ((Bool, (any Error)?) -> Void)?)](./pushpanel%28_,completion%29.md)
  Pushes a new panel.
- [func popPanel(completion: ((Bool, (any Error)?) -> Void)?)](./poppanel%28completion%29.md)
  Pops the top panel from the overlay’s panel stack.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplate/hidepanel(completion:))*