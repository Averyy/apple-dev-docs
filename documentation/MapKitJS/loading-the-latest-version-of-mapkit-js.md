# Loading the latest version of MapKit JS

**Framework**: MapKit JS

Link to the most recent autoupdating version of MapKit JS, or a version of your choice.

#### Overview

When you include a map element on your webpage, your webpage loads a version of MapKit JS. Load the most recent version of MapKit JS available whenever possible.

Load MapKit JS directly using a `<script>` tag, or by using the `@apple/mapkit-loader` package; save payload size and bandwidth by specifying only the libraries that you need. Increase the security of your website by implementing a Content Security Policy.

#### Load with the Mapkit Js Loader

The `@apple/mapkit-loader` package is a convenient way to load MapKit JS: it provides a single API that you can use to load MapKit JS directly from your JavaScript or TypeScript source code, without having access to HTML.

In the example below, the `mapkit` namespace object is available as soon as the `load()` function resolves:

```javascript
import { load } from "@apple/mapkit-loader";

const mapkit = await load({
  token: "Your MapKit JS token",
  language: "en-US",
  libraries: ["services", "full-map", "geojson"],
});
```

See [`Creating a Maps token`](creating-a-maps-token.md) to obtain a Maps token and insert that into the `token` property. To load more efficiently, instruct MapKit JS to load only the specific libraries that you need by setting the `libraries` array.

Your application code needs to call the `load()` function as early as possible, but only when it needs MapKit JS. The [`MapKit JS Loader project repository`](https://developer.apple.comhttps://github.com/apple/mapkit-loader) contains additional examples about integrating with different Web Frameworks and server-side rendering.

The package automatically resolves type definitions for the interfaces that you load.

#### Select Mapkit Js Libraries

Pick only the interfaces you need to optimize your app load time. MapKit JS divides its interfaces into libraries that you can specify when loading the framework:

You can set the libraries to load statically by defining them in the `libraries` options array on the MapKit JS Loader `load()` function, within a script tag in the `data-libraries` attribute.

You may load additional libraries using the `mapkit.load()` method after MapKit JS initialization. The `mapkit.init()` method also offers a `libraries` property in [`MapKitInitializationOptions`](mapkitinitializationoptions.md).

#### Load with a Script Tag

Load MapKit JS through autoupdate URLs (which are backward-compatible with previous MapKit JS versions), as in the example below:

```html
<script src="https://cdn.apple-mapkit.com/mk/5.x.x/mapkit.core.js"
    crossorigin async
    data-callback="initMapKit"
    data-libraries="services,full-map,geojson"
    data-token="Your MapKit JS token"></script>
```

See [`Creating a Maps token`](creating-a-maps-token.md) to obtain a Maps token and insert the token into the `data-token` attribute. To load MapKit JS more efficiently, specify that MapKit JS only loads the specific libraries that you need by setting the `data-libraries` attribute.

Once the callback triggers, `mapkit` is available as a global object. Install `@types/apple-mapkit` separately to access its type definitions.

##### Select Script Element Attributes

The `script` tag you use to load MapKit JS supports several attribute elements that allow you to customize the loading of the framework to support only the features you need.

```html
<script src="https://cdn.apple-mapkit.com/mk/5.x.x/mapkit.core.js"
    crossorigin async
    data-callback="initMapKit"
    data-libraries="services,full-map,geojson"
    data-token="Your MapKit JS token"></script>
```

In this example, MapKit JS self-initializes and self-loads the specified libraries, and then triggers the callback when loading of the libraries is complete. You can choose the MapKit JS interfaces and features by changing the libraries to load.

The script tag value is the URL that points to `mapkit.core.js`, the principal JavaScript file for MapKit JS, for all versions of the src attribute of this script tag. The `script` tag, and all the examples here, include two additional attributes recommended for use with MapKit JS:

The data attributes you can set on the `script` element are:

#### Choose Specific Releases Using Semantic Versioning

MapKit JS follows semantic versioning with each release. As a result, you have full control over when to upgrade to a new version of MapKit JS. Each version follows the standard semantic versioning pattern `MAJOR.MINOR.PATCH,` which conveys the following information:

A backward-compatible new release that contains only bug fixes increases the patch version; a backward-compatible new release that contains new features or functionality increases the minor version. A new release that changes the API, so it’s no longer backward-compatible, increases the major version.

In this example, the script tag pins the major version at `5`, and the server automatically selects the latest `minor.patch` version. It’s also possible to request more specific versions by specifying the patch version, as the following example shows:

```html
<script src="https://cdn.apple-mapkit.com/mk/5.0.x/mapkit.core.js"
    crossorigin async
    data-callback="initMapKit"
    data-libraries="services,full-map,geojson"
    data-token="Your MapKit JS token"></script>
```

Here, the script tag pins the `major.minor` version at `5.0`, and the server automatically selects the latest patch version.

Autoupdate URLs have a cache time of 5 minutes.

#### Use Explicitly Versioned Urls

If your code depends upon a specific MapKit JS version, each version of MapKit JS has a unique URL. Linking to a specific version ensures that your app always gets that exact version of MapKit JS.

MapKit JS Loader provides a `version` options property for setting the desired version.

Below are few examples of version URLs, loading MapKit JS with a `<script>` tag:

```html
<script src="https://cdn.apple-mapkit.com/mk/5.0.0/mapkit.core.js"
    crossorigin async
    data-callback="initMapKit"
    data-libraries="services,full-map,geojson"
    data-token="Your MapKit JS token"></script>
```

```html
<script src="https://cdn.apple-mapkit.com/mk/5.0.1/mapkit.core.js"
    crossorigin async
    data-callback="initMapKit"
    data-libraries="services,full-map,geojson"
    data-token="Your MapKit JS token"></script>
```

```html
<script src="https://cdn.apple-mapkit.com/mk/5.1.0/mapkit.core.js"
    crossorigin async
    data-callback="initMapKit"
    data-libraries="services,full-map,geojson"
    data-token="Your MapKit JS token"></script>
```

Browsers cache version URLs for a longer time. Use versioned URLs if you want to be in full control of when MapKit JS updates and get the benefits of browser caching.

#### Load the Full Bundle of Mapkit Js

> **Note**:  The full bundle does not contain newer features like [`LookAround`](lookaround.md).

A full browser bundle is also available, but it isn’t recommended in production for performance reasons. With the full bundle, the full MapKit JS interfaces are available as soon as the script tag loads.

```javascript
<script
  src="https://cdn.apple-mapkit.com/mk/5.x.x/mapkit.js"
  crossorigin defer
></script>
```

This example uses the `defer` attribute in place of `async`. With this attribute, the browser evaluates the script only after the browser fully downloads and parses the HTML. This prevents `mapkit.js` from blocking the page load, but the `mapkit` instance isn’t available to the embedded `<script>` blocks in HTML until loading and evaluation is complete.

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

MapKit JS Loader doesn’t support loading the full bundle.

#### Implement a Content Security Policy

To mitigate possible security attacks such as data injection or Cross-Site Scripting (XSS), consider implementing Content Security Policy (CSP) in your app. MapKit JS supports a `nonce`-based CSP.

When implementing a CSP in MapKit JS:

- The website must set the `nonce` attribute on the script element when loading Mapkit JS.
- MapKit JS needs to load workers and blob URLs, and connect to and load images from the MapKit CDN.
- Complete rendering of the map and Look Around requires Web Assembly.

The following example shows possible CSP directives:

```other
script-src 'nonce-{nonce-value}' 'wasm-unsafe-eval';
style-src 'nonce-{nonce-value}';
img-src https://*.apple-mapkit.com blob:;
connect-src https://*.apple-mapkit.com blob:;
worker-src https://*.apple-mapkit.com blob:;
frame-src https://*.apple-mapkit.com;
```

MapKit JS Loader provides a `nonce` options property for the value.

The following example demonstrates a script tag with a `nonce` value:

```html
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
- [class mapkit](mapkit.md)
  The JavaScript API for embedding Apple Maps on your website.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/loading-the-latest-version-of-mapkit-js)*