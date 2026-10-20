# displaySyncEnabled

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the layer synchronizes its updates to the display’s refresh rate.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.13+

## Declaration

```swift
var displaySyncEnabled: Bool { get set }
```

```objc
@property BOOL displaySyncEnabled;
```

#### Discussion

Set this value to [`true`](../../Swift/true.md) to synchronize the presentation of the layer’s contents with the display’s refresh, also known as *vsync* or *vertical sync*. If [`false`](../../Swift/false.md), the layer presents new content more quickly, but possibly with brief visual artifacts (*screen tearing*).

The default value is [`true`](../../Swift/true.md).

## See Also

### Configuring Presentation Behavior
- [var presentsWithTransaction: Bool](./presentswithtransaction.md)
  A Boolean value that determines whether the layer presents its content using a Core Animation transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cametallayer/displaysyncenabled)*