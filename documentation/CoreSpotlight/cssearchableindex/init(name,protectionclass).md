# init(name:protectionClass:)

**Framework**: Core Spotlight  
**Kind**: init  
**Role**: Initializer

Returns an on-device index with the specified name and data protection class.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
init(name: String, protectionClass: FileProtectionType?)
```

```objc
- (instancetype) initWithName:(NSString *) name protectionClass:(NSFileProtectionType) protectionClass;
```

## Mentions

- [Adding your app’s content to Spotlight indexes](../adding-your-app-s-content-to-spotlight-indexes.md)

#### Return Value

An index that can handle items within the specified protection class.

#### Discussion

Use this method to specify a protection class for an index. You can specify a default protection class for index items in the entitlements for your app.

## Parameters

- `name`: A name that pertains to your custom organization.
- `protectionClass`: The file protection class. Acceptable values are [`none`](../../Foundation/fileprotectiontype/none.md), [`complete`](../../Foundation/fileprotectiontype/complete.md), [`completeUnlessOpen`](../../Foundation/fileprotectiontype/completeunlessopen.md), or [`completeUntilFirstUserAuthentication`](../../Foundation/fileprotectiontype/completeuntilfirstuserauthentication.md).

## See Also

### Creating an index
- [class func `default`() -> Self](./default%28%29.md)
  Returns the default on-device index.
- [init(name: String)](./init%28name%29.md)
  Returns an on-device index with the specified name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableindex/init(name:protectionclass:))*