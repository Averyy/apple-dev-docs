# init()

**Framework**: BrowserEngineKit  
**Kind**: init  
**Role**: Initializer

Creates a transaction coordinator.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
init() throws
```

```objc
+ (BELayerHierarchyHostingTransactionCoordinator *) coordinatorWithError:(NSError **) error;
```

#### Discussion

This initializer can fail and throw an error if the process fails to retrieve a connection to the system’s Core Animation rendering server.

This method takes ownership of the port send right.

## See Also

### Creating a transaction coordinator
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a transaction coordinator from an encoded representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/layerhierarchyhostingtransactioncoordinator/init())*