# showPanel(_:completion:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Shows an overlay with the specified panel.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
func showPanel(_ panel: CPMapPanel, completion: ((Bool, (any Error)?) -> Void)? = nil)
```

```swift
func showPanel(_ panel: CPMapPanel) async throws -> Bool
```

```objc
- (void) showPanel:(CPMapPanel *) panel completion:(void (^)(BOOL success, NSError *error)) completion;
```

## Parameters

- `panel`: The panel to display.
- `completion`: An optional block called when the overlay has been shown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplate/showpanel(_:completion:))*