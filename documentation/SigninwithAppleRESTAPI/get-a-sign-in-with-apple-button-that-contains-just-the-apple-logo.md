# Get a Sign in with Apple button that contains just the Apple logo.

**Framework**: SigninwithAppleRESTAPI  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Generate a Sign in with Apple button image containing just the Apple logo.

## Mentions

- [Incorporating Sign in with Apple into other platforms](../SigninwithApple/incorporating-sign-in-with-apple-into-other-platforms.md)

### Discussion

Use this file to customize and embed your button of choice in your application or service. You can also test and preview custom buttons at [Sign in with Apple Button](https://appleid.apple.com/signinwithapple/button). For more information, see [Incorporating Sign in with Apple into other platforms](../SigninwithApple/incorporating-sign-in-with-apple-into-other-platforms.md).

## Endpoint

`GET https://appleid.cdn-apple.com/appleid/button/logo`

## Parameters

### Query Parameters

- `border` (boolean): A Boolean value that determines whether the button image has a border.

  **Default**: `false`
- `border_radius` (int32): The corner radius for the button image in points.

  **Default**: `15`; **Minimum**: `0`; **Maximum**: `50`
- `color` (string): The background color for the button image. The possible values are `white` and `black`.

  **Default**: `black`
- `scale` (int32): The scale of the button image.

  **Default**: `1`; **Minimum**: `1`; **Maximum**: `6`
- `size` (int32): The size, in points, of the Apple logo. This sets both the width and the height of the logo since the button is square.

  **Default**: `30`; **Minimum**: `30`; **Maximum**: `64`

## Responses

- `200` OK (`binary`, `image/png`): Request succeeded.
- `404` Not Found (`application/json`): Resource not found.

## See Also

### Sign in with Apple buttons
- [Get a Sign in with Apple button that is center-aligned.](./get-a-sign-in-with-apple-button-that-is-center-aligned.md)
  Generate a Sign in with Apple button with center-aligned text.
- [Get a Sign in with Apple button that is left-aligned.](./get-a-sign-in-with-apple-button-that-is-left-aligned.md)
  Generate a Sign in with Apple button with left-aligned text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/signinwithapplerestapi/get-a-sign-in-with-apple-button-that-contains-just-the-apple-logo.)*