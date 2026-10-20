# streamingClients

**Framework**: Core Media I/O  
**Kind**: property  
**Role**: Instance Property

An array of clients of the stream.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
var streamingClients: [CMIOExtensionClient] { get }
```

```objc
@property (atomic, copy, readonly) NSArray<CMIOExtensionClient *> * streamingClients;
```

#### Discussion

This property is key-value observable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstream/streamingclients)*