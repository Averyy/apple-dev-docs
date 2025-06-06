# Creating a Maps token

**Framework**: MapKit JS

Generate your token to access MapKit services with proper authorization.

#### Overview

MapKit JS uses tokens to authenticate map initializations and other API requests. You create a Maps token through your [`Apple Developer Account`](https://developer.apple.comhttps://developer.apple.com/account), and then use the token to access MapKit JS services for displaying maps and points of interest on them.

##### Create the Maps Token

To create a Maps token, follow these steps:

1. Go to [`Apple Developer Account`](https://developer.apple.comhttps://developer.apple.com/account) and log in with your Apple Developer credentials.
2. Under [`Certificates, Identifiers & Profiles`](https://developer.apple.comhttps://developer.apple.com/account/ios/certificate), click Services in the sidebar.
3. Under the Maps section, click Configure.
4. Click Tokens at the top of the Usage Dashboard.
5. At the top of the list, click Tokens (+).
6. In the Create Maps Token overlay, select the type of token under Token Type: Embed API, MapKit JS, Server API, or Web Snapshots
7. Under Restriction Type, select the restriction type: Domain or None.
8. If you select Domain, select the duration under Domain Token Validation Duration: No Expiration, 30 Days, 90 Days, 180 Days, or Other. If you select Other, specify the expiration date. Provide a comma-delimited list of domains under Websites.
9. Provide an optional description under Token Description.
10. Click Create to create the token.

The token appears in the list under Website domains. Click the copy icon to copy the token to your clipboard, or click the name of the token to view its details. Use your new token to access MapKit JS services through [`mapkit`](mapkit.md).

If you need to revoke your token, click Revoke. This invalidates the token and you can no longer use it with MapKit JS.

## See Also

- [Displaying place information using the Maps Embed API](displaying-place-information-using-the-maps-embed-api.md)
  Show place information on a map using a URL.
- [Loading the latest version of MapKit JS](loading-the-latest-version-of-mapkit-js.md)
  Link to the most recent autoupdating version of MapKit JS, or a version of your choice.
- [mapkit](mapkit.md)
  The JavaScript API for embedding Apple Maps on your website.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/creating-a-maps-token)*