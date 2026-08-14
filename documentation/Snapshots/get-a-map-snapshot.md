# Create a Maps Web Snapshot

**Framework**: Maps Web Snapshots  
**Kind**: httpRequest

Generates a map image with characteristics that you provide in the query parameters.

**Availability**:
- Maps Web Snapshots 1.0+

## Mentions

- [Generating a URL and Signature to Create a Maps Web Snapshot](generating-a-url-and-signature-to-create-a-maps-web-snapshot.md)

#### Discussion

Use the Snapshot URL query parameters to define characteristics of the map image such as dimensions, language, color scheme, and more.

You must sign every Snapshot URL request and include the signature as the final parameter. For details and example code, see [`Generating a URL and Signature to Create a Maps Web Snapshot`](generating-a-url-and-signature-to-create-a-maps-web-snapshot.md).

## Endpoint

`GET https://snapshot.apple-mapkit.com/api/v1/snapshot`

## Parameters

- `teamId` (string): **Only use this parameter if you don’t provide a token parameter.** Your Apple Developer Team ID. For more information, see [`Creating a Maps identifier and a private key`](https://developer.apple.com/documentation/applemapsserverapi/creating-a-maps-identifier-and-a-private-key).
- `keyId` (string): **Only use this parameter if you don’t provide a token parameter.** Your MapKit JS Key ID. For more information, see [`Creating a Maps identifier and a private key`](https://developer.apple.com/documentation/applemapsserverapi/creating-a-maps-identifier-and-a-private-key).
- `signature` (string): **Only use this parameter if you don’t provide a token parameter.** A Base64, URL-encoded signature that signs the request path and query parameters. The signature must be the last parameter in the request URL; otherwise, the request returns status code `401 Unauthorized`. See [`Generating a URL and Signature to Create a Maps Web Snapshot`](generating-a-url-and-signature-to-create-a-maps-web-snapshot.md).
- `center` (string) *(required)*: The center of the map. You can specify `center` as coordinates, as an address, or with the string `auto` when you add annotations and overlays. Provide coordinates as a string with the latitude and longitude separated by a comma, such as: ```javascript
center=37.78%2C-122.42
``` If you specify `center` as coordinates, the latitude must be in the range `(-90, 90)` and longitude must be in the range `(-180, 180)`. A geocoded address is a valid value for the `center` parameter, such as: ```javascript
center=San%20Francisco%20City%20Hall%20in%20San%20Francisco%2C%20California
``` The string `auto` is also a valid value for the `center` parameter, for example: ```javascript
center=auto
``` If you specify `center=”auto”`, the Web Map Snapshot API returns a map that includes all overlays or annotations. The API requires `annotations` or `overlays` when you use `center=”auto”`.
- `z` (float): The zoom level of the map. The Web Map Snapshot API ignores the `z` parameter when you specify `auto` for the `center` parameter, or when you specify both `spn` and `z` parameters.
- `spn` (string): A comma-separated coordinate span that indicates how much of the map Web Map Snapshots API displays around the map’s center. The latitude must be in the range of `(0, 90)`, and the longitude must be in the range `(0, 180)`. The latitude and longitude delta parameters must be positive numbers; the API treats negative numbers as `0`. The Web Map Snapshot API ignores the `spn` parameter if you specify `auto` for the `center` parameter. If you provide both `z` and `spn` parameters, the value for `spn` takes precedence over `z`.
- `size` (string): The size of the image in pixels. Specify the `size` as width and height integers separated by the character `x`. For example, `640x480` creates an image 640 pixels wide and 480 pixels tall. The width and height must be within the range of `[50, 640]`.
- `scale` (int32): The pixel density of the image. `scale=2` returns an image intended for 2x Retina displays. Setting `scale` to values greater than `1` increases the number of pixels in the generated image.
- `t` (string): The map type.
- `colorScheme` (string): The color scheme of the map. The `dark` color scheme only applies to the `standard` and `mutedStandard` map types.
- `poi` (boolean): A Boolean value that indicates whether to show points of interest on the map. To hide points of interest, set `poi=0`.
- `lang` (string): The language that Maps Web Snapshots API uses for labels on the map. Supported values are locale IDs, such as `en-GB` or `es-MX`.
- `annotations` ([Annotation]): An array of annotations to display on the map, which you specify as JSON [`Annotation`](annotation.md) objects. Annotations layer on top of the map in the order you specify in the request.
- `overlays` ([Overlay]): An array of overlays to display on the map, which you specify as an array of JSON [`Overlay`](overlay.md) objects.
- `overlayStyles` ([OverlayStyle]): A JSON array of overlay styles. This object allows you to reuse style values on different overlays.
- `imgs` ([Image]): An array of custom images to annotate the map, specified as an array of JSON [`Image`](image.md) objects.
- `referer` (string): **Only use this parameter if you don’t provide a token parameter.** The `referer` string value to match against the request’s `Referer` header value. Requests that don’t match the `referer` parameter fail with HTTP status code `401 Unauthorized`. Set a referrer restriction through the `referer` parameter.
- `expires` (int64): **Only use this parameter if you don’t provide a token parameter.** The time in seconds from epoch at which the request expires. Expired requests fail with HTTP status code `401 Unauthorized`. Set an expiration through the `expires` parameter.
- `token` (string): A developer’s Maps token. For information on how to create a Maps token, see [`Creating a Maps token`](https://developer.apple.com/documentation/mapkitjs/creating-a-maps-token).

## See Also

- [Generating a URL and Signature to Create a Maps Web Snapshot](generating-a-url-and-signature-to-create-a-maps-web-snapshot.md)
  Create a Snapshot URL and generate a signature to validate the request.
- [object Annotation](annotation.md)
  An object for a Snapshot URL that describes annotation characteristics.
- [object Overlay](overlay.md)
  A JSON object for a Snapshot URL that describes overlay shape characteristics, including points for the overlay and styles such as width, color, and dash pattern.
- [object OverlayStyle](overlaystyle.md)
  A  JSON object that describes reusable styles for an overlay.
- [object Image](image.md)
  A JSON object for a Snapshot URL that describes the characteristics of custom images to use for map annotations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/snapshots/get-a-map-snapshot)*