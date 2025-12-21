# displaySyncEnabled

**Framework**: Core Animation  
**Kind**: property

A Boolean value that determines whether the layer synchronizes its updates to the display’s refresh rate.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.13+

## Declaration

```swift
var displaySyncEnabled: Bool { get set }
```

#### Discussion

Set this value to [`true`](https://developer.apple.com/documentation/Swift/true) to synchronize the presentation of the layer’s contents with the display’s refresh, also known as  or . If [`false`](https://developer.apple.com/documentation/Swift/false), the layer presents new content more quickly, but possibly with brief visual artifacts ().

The default value is [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [var presentsWithTransaction: Bool](cametallayer/presentswithtransaction.md)
  A Boolean value that determines whether the layer presents its content using a Core Animation transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cametallayer/displaysyncenabled)*