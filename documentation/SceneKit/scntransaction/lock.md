# lock()

**Framework**: SceneKit  
**Kind**: method

Attempts to acquire a recursive spinlock to ensure the validity of values you retrieve during the transaction.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class func lock()
```

#### Discussion

SceneKit’s data model is thread-safe in that it ensures that internal data structures will not be corrupted by concurrent attempts to modify their contents from multiple threads. However, this model does not guarantee the validity of values you read from scene graph objects after returning them.

For example, consider the following operation:

```objc
_node.position = SCNVector3Make(_node.position.x, _node.position.y + 10, _node.position.z);
```

The intent of this line is to move a node by ten units. But if another thread modifies the node’s [`position`](scnnode/position.md) property concurrently, the new position value could be unexpected. If your app modifies the scene graph from multiple threads, use a transaction lock to ensure that your modifications take effect as intended.

```objc
[SCNTransaction lock];
_node.position = SCNVector3Make(_node.position.x, _node.position.y + 10, _node.position.z);
[SCNTransaction unlock];
```

If another thread currently holds a lock on the transaction, calling [`lock()`](scntransaction/lock().md) has no effect.

## See Also

- [class func unlock()](scntransaction/unlock.md)
  Relinquishes a previously acquired transaction lock.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntransaction/lock())*