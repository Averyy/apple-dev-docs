# init(apiToken:)

**Framework**: CloudKit  
**Kind**: init  
**Role**: Initializer

Creates a fetch operation for the specified API token.

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
convenience init(apiToken APIToken: String)
```

```objc
- (instancetype) initWithAPIToken:(NSString *) APIToken;
```

## Parameters

- `APIToken`: The API token that allows access to an app’s container.

## See Also

### Creating a Fetch Token Operation
- [init()](./init%28%29.md)
  Creates an empty fetch operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchwebauthtokenoperation/init(apitoken:)-14712)*