# hasChanges

**Framework**: Core Data  
**Kind**: property

A Boolean value that indicates whether the context has uncommitted changes.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var hasChanges: Bool { get }
```

#### Discussion

If you are observing this property using key-value observing (KVO) you should not touch the context or its objects within your implementation of doc://com.apple.documentation/documentation/objectivec/nsobject/1416553-observevalue for this notification. (This is because of the intricacy of the locations of the KVO notifications—for example, the context may be in the middle of an undo operation, or repairing a merge conflict.) If you need to send messages to the context or change any of its managed objects as a result of a change to the value of `hasChanges`, you must do so after the call stack unwinds (typically using doc://com.apple.documentation/documentation/objectivec/nsobject/1416176-perform or a similar method).

##### Special Considerations

In macOS 10.6 and later, this property is [`Key-value observing`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/KVO.html#//apple_ref/doc/uid/TP40008195-CH16) compliant.

## See Also

- [func save() throws](nsmanagedobjectcontext/save.md)
  Attempts to commit unsaved changes to registered objects to the context’s parent store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/haschanges)*