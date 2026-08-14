# cancel(promise)

**Framework**: MapKit JS  
**Kind**: method

Cancels a request using the provided request promise.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
cancel(promise: Promise<unknown>): boolean;
```

## Mentions

- [Migrating from Version 5 to Version 6](migrating-from-version-5-to-version-6.md)

#### Return Value

`true` if the server cancels the pending search request.

#### Discussion

Sometimes you need to cancel a request, either because a person initiates the cancellation or moves on to another activity.

The preferred way to cancel a request is to use an `AbortSignal`. Pass the `signal` property of an `AbortController` to the service method’s options, and call `abort()` on the controller when you need to cancel the request.

Alternatively, you can cancel a request by passing its returned promise to the [`cancel()`](service/cancel.md) method:

```javascript
const search = new mapkit.Search();
const promise = search.search("coffee");

// Cancel the request:
search.cancel(promise);
```

## Parameters

- `promise`: Pass the promise returned from the service method. Passing an invalid promise or the promise of a completed request has no effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/service/cancel)*