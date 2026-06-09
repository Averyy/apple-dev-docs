# RequestError

**Framework**: MapKit JS  
**Kind**: class

The error that a service method’s returned promise rejects with when a request fails.

**Availability**:
- MapKit JS 6.0+

## Declaration

```swift
class RequestError extends Error
```

## Mentions

- [Migrating from Version 5 to Version 6](migrating-from-version-5-to-version-6.md)

#### Discussion

When a [`Service`](service.md) method’s returned promise rejects, the rejection value is a [`RequestError`](requesterror.md). The [`message`](requesterror/message.md) property contains a [`ConfigurationErrorStatus`](configurationerrorstatus.md) value that describes the error.

```javascript
const search = new mapkit.Search();

try {
    const data = await search.search("coffee");
} catch (error) {
    if (error.message === "Too Many Requests") {
        // Handle rate limiting.
    }
}
```

## Topics

### Properties
- [message](requesterror/message.md)
  The error message describing the request failure.

## Relationships

### Inherits From
- [Error](doc://com.apple.mapkitjs/__unknown__/Error)

## See Also

- [class Service](service.md)
  An abstract class that provides common interfaces for service objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/requesterror)*