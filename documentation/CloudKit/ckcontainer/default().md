# default()

**Framework**: CloudKit  
**Kind**: method  
**Role**: Type Method

Returns the app’s default container.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class func `default`() -> CKContainer
```

```objc
+ (CKContainer *) defaultContainer;
```

## Mentions

- [Designing and Creating a CloudKit Database](../designing-and-creating-a-cloudkit-database.md)

## Discussion

Use this method to retrieve your app’s default container. This is the one you typically use to store your app’s data. If you want the container for a different app, create a container using the [`init(identifier:)`](./init%28identifier%29.md) method.

During development, the container uses the development environment. When you release your app, the container uses the production environment.

## See Also

### Creating Containers
- [init(identifier: String)](./init%28identifier%29.md)
  Creates a container for the specified identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckcontainer/default())*