# init()

**Framework**: CloudKit  
**Kind**: init  
**Role**: Initializer

Creates an empty fetch operation.

**Availability**:
- iOS 9.2+
- iPadOS 9.2+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.1+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
init()
```

```objc
- (instancetype) init;
```

## Discussion

You must set [`apiToken`](./apitoken.md) before you execute the operation or add it to a queue.

## See Also

### Creating a Fetch Token Operation
- [convenience init(apiToken: String)](./init%28apitoken%29-14712.md)
  Creates a fetch operation for the specified API token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchwebauthtokenoperation/init())*