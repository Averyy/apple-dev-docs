# pushPanel(_:completion:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Pushes a new panel.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
func pushPanel(_ panel: CPMapPanel, completion: ((Bool, (any Error)?) -> Void)? = nil)
```

```swift
func pushPanel(_ panel: CPMapPanel) async throws -> Bool
```

```objc
- (void) pushPanel:(CPMapPanel *) panel completion:(void (^)(BOOL success, NSError *error)) completion;
```

## Parameters

- `panel`: The panel to push.
- `completion`: An optional block called when the panel has been pushed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplate/pushpanel(_:completion:))*