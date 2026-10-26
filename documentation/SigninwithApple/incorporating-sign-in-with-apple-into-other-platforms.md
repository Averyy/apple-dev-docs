# Incorporating Sign in with Apple into other platforms

**Framework**: Sign in with Apple  
**Role**: Article

Add Sign in with Apple capabilities to apps that can’t directly access Sign in with Apple JS.

#### Overview

To add Sign in with Apple to apps that don’t have access to the [Sign in with Apple JS](../SigninwithAppleJS/SigninwithAppleJS.md) framework, you control the sign-in request manually. Perform this request by adding a custom Sign in with Apple button, sending the required query parameters, handling the return request, and returning control back to the app.

##### Add a custom Sign in with Apple button

Apple provides three secure HTTP URLs that generate Sign in with Apple button images corresponding to three modes: center-aligned, left-aligned, and logo only. Entering one of these URLs in a browser triggers the download of the related button image as a PNG file. Use this file to customize and embed your button of choice in your application or service. You can also test and preview custom buttons at [Sign in with Apple Button](https://appleid.apple.com/signinwithapple/button).

Customize the button image by adding query parameters to the URL. If you send invalid query parameters to the endpoint URL, the server returns a `404 Page Not Found` error.

For a center-aligned button, use the secure HTTP URL `https://appleid.cdn-apple.com/appleid/button`, as in this example:

```console
curl --get "https://appleid.cdn-apple.com/appleid/button" \
-H 'content-type: application/json; charset=UTF-8' \
-d 'height=HEIGHT' \
-d 'width=WIDTH' \
-d 'color=COLOR' \
-d 'border=BORDER' \
-d 'type=TYPE' \
-d 'border_radius=BORDER_RADIUS' \
-d 'scale=SCALE' \
-d 'locale=LOCALE' \
-o FILENAME
```

You can customize the button with the following attributes:

- **`height`**: The height of the button image in points. The minimum and maximum values are `30` and `64`, respectively. The default is `30`.
- **`width`**: The width of the button image in points. The minimum and maximum values are `130` and `375`, respectively. The default is `140`.
- **`color`**: The background color for the button image. The possible values are `white` and `black`. The default is `black`.
- **`border`**: A Boolean value that determines whether the button image has a border. The default is `false`.
- **`type`**: The type of button image returned. The possible values are `sign-in` and `continue`. The default is `sign-in`.
- **`border_radius`**: The corner radius for the button image in points. The minimum and maximum values are `0` and `50`, respectively. The default  is `15`.
- **`scale`**: The scale of the button image. The minimum and maximum values are `1` and `6`, respectively. The default is `1`.
- **`locale`**: The language used for text on the button. The possible values are `ar_SA`, `ca_ES`, `cs_CZ`, `da_DK`, `de_DE`, `el_GR`, `en_GB`, `en_US`, `es_ES`, `es_MX`, `fi_FI`, `fr_CA`, `fr_FR`, `hr_HR`, `hu_HU`, `id_ID`, `it_IT`, `iw_IL`, `ja_JP`, `ko_KR`, `ms_MY`, `nl_NL`, `no_NO`, `pl_PL`, `pt_BR`, `pt_PT`, `ro_RO`, `ru_RU`, sk_SK, `sv_SE`, `th_TH`, `tr_TR`, `uk_UA`, `vi_VI`, `zh_CN`, `zh_HK`, and `zh_TW`.

For a left-aligned button, use the secure HTTP URL `https://appleid.cdn-apple.com/appleid/button/left`, as in this example:

```console
curl --get "https://appleid.cdn-apple.com/appleid/button/left" \
-H 'content-type: application/json; charset=UTF-8' \
-d 'height=HEIGHT' \
-d 'width=WIDTH' \
-d 'color=COLOR' \
-d 'border=BORDER' \
-d 'type=TYPE' \
-d 'border_radius=BORDER_RADIUS' \
-d 'scale=SCALE' \
-d 'locale=LOCALE' \
-o FILENAME
```

You can customize the button using the same attributes you use for customizing a center-aligned button, shown above, and the following attributes:

- **`label-position`**: The label’s distance, in points, from the left side of the button. The minimum and maximum values are `0` and `182`, respectively. The default is `0`. The value can’t be larger than half of the width of the button. The label auto-adjusts to fit the recommended margins.
- **`logo-position`**: The Apple logo’s distance, in points, from the left side of the button. The minimum and maximum values are `0` and `182`, respectively. The default is `0`. The value can’t be larger than half of the width of the button. The logo auto-adjusts to fit the recommended margins.
- **`logo-size`**: The size of the logo. The values are `small`, `medium`, and `large`.

For a button with the Apple logo only, use the secure HTTP URL `https://appleid.cdn-apple.com/appleid/button/logo`, as in this example:

```console
curl --get "https://appleid.cdn-apple.com/appleid/button/logo" \
-H 'content-type: application/json; charset=UTF-8' \
-d 'label-position=LABEL_POSITION' \
-d 'logo-position=LOGO_POSITION' \
-d 'logo-size=LOGO_SIZE' \
-o FILENAME
```

You can customize the logo button with the following attributes:

- **`size`**: The size, in points, of the Apple logo. This sets both the width and the height of the logo since the button is square.
- **`color`**: The background color for the button image. The possible values are `white` and `black`. The default is `black`.
- **`border`**: A Boolean value that determines whether the button image has a border. The default is `false`.
- **`border_radius`**: The corner radius for the button image in points. The minimum and maximum values are `0` and `50`, respectively. The default  is `15`.
- **`scale`**: A multiplier that increases the width and height of the button. For example, a value of `2` doubles the button width and height. The minimum and maximum values are `1` and `6`, respectively. The default is `1`.

When the user clicks any of these button types, open a browser tab with the authorization URL and the authorization query parameters.

##### Send the required query parameters

Direct the authorization request using the HTTP `GET` method to the URL `https://appleid.apple.com/auth/authorize`, as in this example:

```console
curl --get "https://appleid.apple.com/auth/authorize" \
-H 'content-type: application/json; charset=UTF-8' \
-d 'client_id=CLIENT_ID' \
-d 'redirect_uri=REDIRECT_URI' \
-d 'response_type=RESPONSE_TYPE' \
-d 'scope=SCOPE' \
-d 'response_mode=RESPONSE_MODE' \
-d 'state=STATE' \
-d 'nonce=NONCE'
```

The URL contains the following parameters:

- **`client_id`**: Required. The identifier (App ID or Services ID) for your app. The identifier must not include your Team ID, to help mitigate the possibility of exposing sensitive data to the end user. Authorization code and refresh token validation requests require this parameter.
- **`redirect_uri`**: Required. The URI to which the authorization redirects. It must include a domain name and can’t be an IP address or `localhost`, and must not contain a fragment identifer (#). For more information, see [Configuring your environment for Sign in with Apple](./configuring-your-environment-for-sign-in-with-apple.md).
- **`response_type`**: Required. The type of response requested. Valid values are `code` and `id_token`. You can request only `code`, or both `code` and `id_token`. Requesting only `id_token` is unsupported. When requesting `id_token`, `response_mode` must be either `fragment` or `form_post`.
- **`scope`**: The amount of user information requested from Apple. Valid values are `name` and `email`. You can request one, both, or none. Use space separation and percent-encoding for multiple scopes; for example, `"scope=name%20email"`.
- **`response_mode`**: The type of response mode expected. Valid values are `query`, `fragment`, and `form_post`. If you requested any scopes, the value must be `form_post`.
- **`state`**: The current state of the request.
- **`nonce`**: A String value used to associate a client session with an ID token. This value is also used to mitigate replay attacks.

If the response contains an error, see [`ErrorResponse`](../SigninwithAppleRESTAPI/errorresponse.md) for the specific error code provided in the response body.

You can also visit [Sign in with Apple button](https://account.apple.com/signinwithapple/button#center-align-button-section) to view and adjust live previews of web-based buttons and get the code.

##### Handle the response

When the Sign in with Apple UI appears in the opened browser tab, the user can sign in and accept any terms and conditions for your app. After Apple processes the authorization request, the handling of the response depends on the value in `response_mode:`

- For the `query` value, the response parameters are added to the [`redirectURI`](../SigninwithAppleJS/clientconfigi/redirecturi.md) value as query parameters, and the browser is redirected to the resulting value.
- For the `fragment` value, the response parameters are added to the `redirectURI` value as a fragment, and the browser is redirected.
- For the `form_post` value, an HTTP `POST` request containing the results of the authorization is sent to the `redirectURI`. The HTTP body contains the result parameters with `application/x-www-form-urlencoded` content type.

A successful response may contain the following parameters:

- **`code`**: A single-use authorization code that’s valid for five minutes. This value is returned if the authorization request contained `code` as a value for `response_type`; otherwise this field is omitted.
- **`id_token`**: A JSON web token containing the user’s identity information. This value is returned if the authorization request contained `code` and `id_token` as a value for `response_type`; otherwise this field is omitted. For more information, see [`id_token`](../SigninwithAppleJS/authorizationi/id_token.md).
- **`state`**: The state value contained in the authorization request, if provided; otherwise this field is omitted.
- **`user`**: A JSON string containing the data requested in the [`scope`](../SigninwithAppleJS/clientconfigi/scope.md) property. The returned data is dependent on what was requested in the in the `scope` parameter and uses the following format: `{ "name": { "firstName": string, "lastName": string }, "email": string }`.

You receive a secure HTTP POST response in which the values returned are dependent on the query parameters used in the request. Use the `state`, `response_type`, and `scope` parameters to control what data is returned. The response is similar to the following example which contains all possible fields:

```json
{
  "code": "cbc78...faa325",
  "id_token": "eyJhb...Ii6uA",
  "state": "ebd019c2-a2d6-4e89-872a-1acab4f851ea",
  "user": {
    "name": {
      "firstName": "Maria",
      "lastName": "Ruiz"
    },
    "email": "ep9ks2tnph@privaterelay.appleid.com"
  }
}
```

If an error occurs, the HTTP body contains the following parameters:

- **`error`**: The returned error code.
- **`state`**: The state contained in the Authorize URL.

> **Note**:  The only error code that might be returned is `user_cancelled_authorize`. This error code is returned if the user clicks Cancel during the web flow.

##### Return control to the app

At the end of the authorization flow, Apple performs a `form_post` to the `redirect_uri` value you provided. At this point, the authorization flow is complete, and it’s your server’s responsibility to persist the data and return control to the app.

Platforms that support custom URL schemes — iOS 12.0 and earlier and Android — must handle the data resulting from the authorization flow by storing it on their app server in the logic of their `redirect_uri` endpoint. You then redirect the custom URL scheme to give control back to the app.

##### Get a Sign in with Apple button

Use the following API endpoints to create a custom Sign in with Apple button:

- [`Get a Sign in with Apple button that is center-aligned.`](../SigninwithAppleRESTAPI/get-a-sign-in-with-apple-button-that-is-center-aligned.md)
- [`Get a Sign in with Apple button that is left-aligned.`](../SigninwithAppleRESTAPI/get-a-sign-in-with-apple-button-that-is-left-aligned.md)
- [`Get a Sign in with Apple button that contains just the Apple logo.`](../SigninwithAppleRESTAPI/get-a-sign-in-with-apple-button-that-contains-just-the-apple-logo.md)

## See Also

### Related Documentation
- [Sign in with Apple JS](../SigninwithAppleJS/SigninwithAppleJS.md)
  Provide users a fast, secure way to sign in to your web service with their Apple Account.
- [Sign in with Apple REST API](../SigninwithAppleRESTAPI/SigninwithAppleRESTAPI.md)
  Communicate between your app servers and Apple’s authentication servers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/signinwithapple/incorporating-sign-in-with-apple-into-other-platforms)*