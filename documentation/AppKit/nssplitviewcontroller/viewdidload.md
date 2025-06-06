# viewDidLoad()

**Framework**: AppKit  
**Kind**: method

Configures the split view controller after its view loads into memory.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func viewDidLoad()
```

#### Discussion

[`NSSplitViewController`](nssplitviewcontroller.md) overrides this method from its parent class, [`NSViewController`](nsviewcontroller.md). If you override this method in a subclass, you must call `super`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewcontroller/viewdidload())*