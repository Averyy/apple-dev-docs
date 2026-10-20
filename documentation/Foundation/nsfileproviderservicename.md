# NSFileProviderServiceName

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

The name used to identify a File Provider service.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct NSFileProviderServiceName
```

```c
typedef NSString * NSFileProviderServiceName;
```

#### Discussion

The team providing the protocol also defines the name. To create a new service’s name:

- Use reverse domain name notation for the interfaces name (for example, `com.example.MyInterface`).
- (Optional) Incorporate versioning by appending a version number to the end of the name (`com.example.MyInterface.v2`).

For more information on defining a service’s protocol, see [Defining the Service’s Protocol](./nsfileproviderservice.md#Defining-the-Services-Protocol).

## Topics

### Initializers
- [init(String)](./nsfileproviderservicename/init%28_%29.md)
  Instantiates a new service name from the provided string.
- [init(rawValue: String)](./nsfileproviderservicename/init%28rawvalue%29.md)
  Instantiates a new service name from the provided string.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Accessing file provider services
- [func getFileProviderServicesForItem(at: URL, completionHandler: ([NSFileProviderServiceName : NSFileProviderService]?, (any Error)?) -> Void)](./filemanager/getfileproviderservicesforitem%28at,completionhandler%29.md)
  Returns the services provided by the File Provider extension that manages the item at the given URL.
- [class NSFileProviderService](./nsfileproviderservice.md)
  A service that provides a custom communication channel between your app and a File Provider extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfileproviderservicename)*