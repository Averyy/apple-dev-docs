# init(options)

**Framework**: MapKit JS  
**Kind**: method

Initializes MapKit JS by providing an authorization callback function and optional language.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
init(options: MapKitInitializationOptions): void;
```

## Mentions

- [Loading the latest version of MapKit JS](loading-the-latest-version-of-mapkit-js.md)

#### Discussion

Unless you wish to explicitly control initialization timing in JavaScript, use `data-token` instead of this method. See [`Loading the latest version of MapKit JS`](loading-the-latest-version-of-mapkit-js.md) for more information.

If you’re using this method, provide the token by setting [`authorizationCallback`](mapkitinitializationoptions/authorizationcallback.md) on a JavaScript object as a function. The [`authorizationCallback`](mapkitinitializationoptions/authorizationcallback.md) function calls `done()` to return the token. [`Creating a Maps token`](creating-a-maps-token.md) shows how to create Maps tokens.

When you create a server endpoint to deliver new tokens to MapKit JS, make an asynchronous request to this endpoint in your [`authorizationCallback`](mapkitinitializationoptions/authorizationcallback.md) function and call `done()` with the result. The following example shows creating a callback that requests a token from a server endpoint and sets a preferred language for the map:

```javascript
mapkit.init({
    authorizationCallback: function(done) {
        fetch("/gettoken")
            .then(res => res.text())
            .then(done);
    },
    language: "es"
});
```

If you don’t set up a server endpoint, you can alternatively set [`authorizationCallback`](mapkitinitializationoptions/authorizationcallback.md) to a function that provides a pregenerated token string.

```javascript
mapkit.init({
    authorizationCallback: function(done) {
        done("your-token-string");
    },
    language: "es"
});
```

An instance of [`mapkit`](mapkit.md) emits a `configuration-change` event after MapKit JS initializes, and an `error` event when initialization fails. You can learn more about both of these events in [`Handling initialization events`](handling-initialization-events.md).

## Parameters

- `options`: MapKit JS initialization options.

## See Also

- [Handling initialization events](handling-initialization-events.md)
  Respond to events that trigger when MapKit JS initializes.
- [interface MapKitInitializationOptions](mapkitinitializationoptions.md)
  Initialization options for MapKit JS.
- [Libraries](mapkit/libraries.md)
  The list of available libraries.
- [loadedLibraries](mapkit/loadedlibraries.md)
  A string that describes the list of loaded libraries.
- [load(libraryNames)](mapkit/load.md)
  Tells MapKit JS which libraries to load.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit/init)*