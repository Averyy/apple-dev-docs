# Handling initialization events

**Framework**: MapKit JS

Respond to events that trigger when MapKit JS initializes.

#### Overview

Unless you wish to explicitly control initialization timing in JavaScript, use `data-token` instead of handling initialization events directly. See [`Loading the latest version of MapKit JS`](loading-the-latest-version-of-mapkit-js.md) for more information.

The `mapkit` object emits two events to indicate the success or failure of a configuration operation. The initialization process configures MapKit JS.

| Event | Summary |
| --- | --- |
| `configuration-change` | The MapKit configuration changes due to either a successful initialization or a refresh. The event has the property `status` (`String`), which indicates the configuration change status. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `Initialized`: MapKit successfully initializes and configures. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `Refreshed`: The MapKit configuration updates. |
| `error` | MapKit fails to initialize. The event has the property `status` (`String`), which indicates the status response. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `Unauthorized`: The provided authorization token is invalid. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `Too Many Requests`: The Maps ID for the authorization token provided exceeds its allowed daily usage. |

MapKit JS invokes these events asynchronously upon success or failure of the initialization request. The example below shows a common use case:

```javascript
mapkit.init({ authorizationCallback: function(done) { done("your-token"); }, ... });
mapkit.addEventListener("configuration-change", function(event) {
    switch (event.status) {
    case "Initialized":
        // MapKit JS initializes and configures.
        break;
    case "Refreshed":
        // The MapKit JS configuration updates.
        break;
    }
});

```

## See Also

- [init](mapkit/init.md)
  Initializes MapKit JS by providing an authorization callback function and optional language.
- [MapKitInitOptions](mapkitinitoptions.md)
  Initialization options for MapKit JS.
- [Libraries](mapkit/libraries.md)
  The list of available libraries.
- [loadedLibraries](mapkit/loadedlibraries.md)
  A string that describes the list of loaded libraries.
- [load](mapkit/load.md)
  Tells MapKit JS which libraries to load.
- [addEventListener](mapkit/addeventlistener.md)
  Subscribes a listener function to an event type.
- [removeEventListener](mapkit/removeeventlistener.md)
  Unsubscribes a listener function from an event type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/handling-initialization-events)*