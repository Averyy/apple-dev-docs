# Loading the latest version of MapKit JS

**Framework**: MapKit JS

Link to the most recent autoupdating version of MapKit JS, or a version of your choice.

#### Overview

When you include a map element on your webpage, your webpage loads a version of MapKit JS. Load the most recent version of MapKit JS available whenever possible. Depending on what features your map uses, you may want to load a specific version. To load more efficiently, you can also specify that MapKit JS only loads the specific elements and libraries that you need.

MapKit JS follows semantic versioning with each release. This means that you, as the developer, have full control over when to upgrade to a new version of MapKit JS. Each version follows the standard semantic versioning pattern `MAJOR.MINOR.PATCH,` which conveys the following information:

- MAJOR — Incompatible API changes
- MINOR — New functionality, but backward-compatible
- PATCH — Backward-compatible bug fixes

A backward-compatible new release that contains only bug fixes increases the patch version; a backward-compatible new release that contains new features or functionality increases the minor version. A new release that changes the API, so it’s no longer backward-compatible, increases the major version.

The recommended mechanism to load MapKit JS is through backward-compatible, autoupdate URLs as the example below shows:

```javascript
<script src="https://cdn.apple-mapkit.com/mk/5.x.x/mapkit.core.js"
    crossorigin async
    data-callback="initMapKit"
    data-libraries="services,full-map,geojson"></script>
```

In this example, the script tag pins the major version at `5`, and the server automatically selects the latest `minor.patch` version. It’s also possible to request more specific versions by specifying the patch version, as the following example shows:

```javascript
<script src="https://cdn.apple-mapkit.com/mk/5.0.x/mapkit.core.js"
    crossorigin async
    data-callback="initMapKit"
    data-libraries="services,full-map,geojson"></script>
```

Here, the script tag pins the `major.minor` version at `5.0`, and the server automatically selects the latest patch version.

Autoupdate URLs have a cache time of 5 minutes.

##### Use Explicitly Versioned Urls

If your code is dependent upon a specific MapKit JS version, each version of MapKit JS has a unique URL. Linking to a version URL ensures that your app always gets that exact version of MapKit JS. Below are few examples of version URLs:

```javascript
<script src="https://cdn.apple-mapkit.com/mk/5.0.0/mapkit.core.js"
    crossorigin async
    data-callback="initMapKit"
    data-libraries="services,full-map,geojson"></script>
```

```javascript
<script src="https://cdn.apple-mapkit.com/mk/5.0.1/mapkit.core.js"
    crossorigin async
    data-callback="initMapKit"
    data-libraries="services,full-map,geojson"></script>
```

```javascript
<script src="https://cdn.apple-mapkit.com/mk/5.1.0/mapkit.core.js"
    crossorigin async
    data-callback="initMapKit"
    data-libraries="services,full-map,geojson"></script>
```

Browsers cache version URLs for a longer time. Use versioned URLs if you want to be in full control of when MapKit JS updates and get the benefits of browser caching.

##### Select Script Element Attributes

The `script` tag you use to load MapKit JS supports several attribute elements that allow you to customize the loading of the framework to support only the features you need.

```javascript
<script
    src="https://cdn.apple-mapkit.com/mk/5.x.x/mapkit.core.js"
    crossorigin async
    data-callback="initMapKit"
    data-libraries="services,full-map,geojson"
    data-token="Your MapKit JS token"></script>
```

In this example, MapKit JS self-initializes and self-loads the specified libraries, and then triggers the callback when loading of the libraries is complete. You can choose the MapKit JS interfaces and features by changing the libraries to load.

The script tag value is the URL that points to `mapkit.core.js`, the principal JavaScript file for MapKit JS, for all versions of the src attribute of this script tag. The `script` tag, and all the examples here, include two additional attributes recommended for use with MapKit JS:

- `crossorigin` — Short for `crossorigin=”anonymous”`, this attribute instructs the browser to connect to the MapKit JS CDN using anonymous credentials mode. This improves performance by allowing subsequent MapKit JS network requests to reuse the same HTTP/2 connection.
- `async` — With this attribute, the browser evaluates the script as soon as it downloads it. This prevents `mapkit.core.js` from blocking the page load, and initializes and loads the MapKit JS libraries as soon as possible. Your app needs to wait for the callback function execution before interacting with the API.

The data attributes you can set on the `script` element are:

- `data-callback` — Required; this is the callback the browser calls when MapKit JS finishes loading.
- `data-language` — The language to set for MapKit JS. A language ID is a language designator followed by an optional region or script designator. Examples of language IDs include: `de` (German), `es-MX`, (Mexican Spanish), and `zh-Hans` (simplified Chinese).
- `data-libraries` — Required; this is a comma-separated list of libraries to load at initialization. See the list of available libraries and the services they provide below.
- `data-token` —` `Required unless you intend to call [`init`](mapkit/init.md) later. See [`Create a Maps Web Snapshot`](https://developer.apple.com/documentation/snapshots/create_a_maps_web_snapshot) to obtain a Maps token.

##### Select Mapkit Js Libraries

Pick only the interfaces you need to optimize your app load time. MapKit JS divides its interfaces into libraries that you can specify when loading the framework:

- `services` — All services interfaces (such as Search and Geocoder) and relevant data types.
- `full-map` — All `mapkit.Map` features and relevant data types.
- `map` — Basic `mapkit.Map` features without overlays, annotations, and relevant data types.
- `overlays` — Overlays, data types, and displays on `mapkit.Map`.
- `annotations` — Annotations, data types, and displays on `mapkit.Map`.
- `geojson` — The GeoJSON importer.
- `user-location` — User location display and controls on `mapkit.Map`.

You can set the libraries to load statically by defining them within a script tag in the `data-libraries` attribute or in the `mapkit.load()` method, or by passing a `libraries` property in the `mapkit.init()` options.

##### Load the Full Bundle of Mapkit Js

A full browser bundle is also available, but it isn’t recommended in production for performance reasons. With the full bundle, the full MapKit JS interfaces are available as soon as the script tag loads.

```javascript
<script
  src="https://cdn.apple-mapkit.com/mk/5.x.x/mapkit.js"
  crossorigin defer
></script>
```

This example uses the `defer` attribute in place of `async`:. With this attribute, the browser evaluates the script only after the browser fully downloads and parses the HTML. This prevents `mapkit.js` from blocking the page load, but the `mapkit` instance isn’t available to the embedded `<script>` blocks in HTML until loading and evaluation is complete.

Alternatively, if you need to load MapKit JS on-demand, create an `HTMLScriptElement`, insert it into the document and use a Javascript Promise, as the following example shows:

```javascript
// This promise resolves when the browser finishes downloading and evaluating MapKit JS.
const mapKitJsLoadedPromise = new Promise(resolve => {
    const element = document.createElement("script");
    element.addEventListener("load", resolve, { once : true });
    element.src = "https://cdn.apple-mapkit.com/mk/5.x.x/mapkit.js"
    element.crossOrigin = "anonymous";
    document.head.appendChild(element);
});
```

The loading of individual libraries isn’t applicable to the full bundle.

##### Implement a Content Security Policy

To mitigate possible security attacks like, data injecting or cross-site Scripting (XSS), consider implementing Content Security Policy (CSP) in your app. MapKit JS supports a `nonce-`based CSP.

When implementing a CSP in MapKit JS:

- The website must set the `nonce` attribute on the script element when loading Mapkit JS.
- MapKit JS needs to load workers, images from and connect to MapKit CDN, and `blob` URLs.

The following example shows possible CSP directives:

```other
script-src 'nonce-{nonce-value}';
style-src 'nonce-{nonce-value}';
img-src https://*.apple-mapkit.com blob:;
connect-src https://*.apple-mapkit.com blob:;
worker-src https://*.apple-mapkit.com blob:;
frame-src https://*.apple-mapkit.com;
```

The following is an example script tag with a `nonce` value:

```javascript
<script 
  src="https://cdn.apple-mapkit.com/mk/5.x.x/mapkit.core.js"
  crossorigin async
  data-callback="initMapKit"
  data-libraries="services,full-map,geojson"
  data-token="Your MapKit JS token"
  nonce="{nonce-value}"
></script> 
```

The following sample is a JavaScript example for loading MapKit JS dynamically:

```javascript
// This promise resolves when MapKit JS downloads and evaluates.
const mapKitJsLoadedPromise = new Promise(resolve => {
    const element = document.createElement("script");
    element.addEventListener("load", resolve, { once : true });
    element.nonce = "{nonce-value}";
    element.src = "https://cdn.apple-mapkit.com/mk/5.x.x/mapkit.js"
    element.crossOrigin = "anonymous";
    document.head.appendChild(element);
});
```

## See Also

- [Displaying place information using the Maps Embed API](displaying-place-information-using-the-maps-embed-api.md)
  Show place information on a map using a URL.
- [Creating a Maps token](creating-a-maps-token.md)
  Generate your token to access MapKit services with proper authorization.
- [mapkit](mapkit.md)
  The JavaScript API for embedding Apple Maps on your website.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/loading-the-latest-version-of-mapkit-js)*