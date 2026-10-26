# Get a Sign in with Apple button that is left-aligned.

**Framework**: SigninwithAppleRESTAPI  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Generate a Sign in with Apple button with left-aligned text.

**Availability**:
- Sign in with Apple REST API 1.0+

## Mentions

- [Incorporating Sign in with Apple into other platforms](../SigninwithApple/incorporating-sign-in-with-apple-into-other-platforms.md)

##### Discussion

Use this file to customize and embed your button of choice in your application or service. You can also test and preview custom buttons at [Sign in with Apple Button](https://appleid.apple.com/signinwithapple/button). For more information, see [Incorporating Sign in with Apple into other platforms](../SigninwithApple/incorporating-sign-in-with-apple-into-other-platforms.md).

## Endpoint

`GET https://appleid.cdn-apple.com/appleid/button/left`

## Parameters

### Query Parameters

- `border` (boolean): A Boolean value that determines whether the button image has a border.

  **Default**: `false`
- `border_radius` (int32): The corner radius for the button image in points.

  **Default**: `15`; **Minimum**: `0`; **Maximum**: `50`
- `color` (string): The background color for the button image. The possible values are `white` and `black`.

  **Default**: `black`
- `height` (int32): The height of the button image in points. The minimum and maximum values are 30 and 64, respectively.

  **Default**: `30`; **Minimum**: `30`; **Maximum**: `64`
- `label-position` (int32): The label’s distance, in points, from the left side of the button. The value can’t be larger than half of the width of the button. The label auto-adjusts to fit the recommended margins.

  **Default**: `0`; **Minimum**: `0`; **Maximum**: `182`
- `locale` (string): The language used for text on the button. The possible values are `ar_SA`, `ca_ES`, `cs_CZ`, `da_DK`, `de_DE`, `el_GR`, `en_GB`, `en_US`, `es_ES`, `es_MX`, `fi_FI`, `fr_CA`, `fr_FR`, `hr_HR`, `hu_HU`, `id_ID`, `it_IT`, `iw_IL`, `ja_JP`, `ko_KR`, `ms_MY`, `nl_NL`, `no_NO`, `pl_PL`, `pt_BR`, `pt_PT`, `ro_RO`, `ru_RU`, `sk_SK`, `sv_SE`, `th_TH`, `tr_TR`, `uk_UA`, `vi_VI`, `zh_CN`, `zh_HK`, and `zh_TW`.
- `logo-position` (int32): The Apple logo’s distance, in points, from the left side of the button. The value can’t be larger than half of the width of the button. The logo auto-adjusts to fit the recommended margins.

  **Default**: `0`; **Minimum**: `0`; **Maximum**: `182`
- `logo-size` (string): The size of the logo. The values are `small`, `medium`, and `large`.
- `scale` (int32): The scale of the button image.

  **Default**: `1`; **Minimum**: `1`; **Maximum**: `6`
- `type` (string): The type of button image returned. The possible values are `sign-in` and `continue`.

  **Default**: `sign-in`
- `width` (int32): The width of the button image in points. The minimum and maximum values are 130 and 375, respectively.

  **Default**: `140`; **Minimum**: `130`; **Maximum**: `375`

## Responses

- `200` OK (`binary`, `image/png`): Request succeeded.
- `404` Not Found (`application/json`): Resource not found.

## See Also

### Sign in with Apple buttons
- [Get a Sign in with Apple button that is center-aligned.](./get-a-sign-in-with-apple-button-that-is-center-aligned.md)
  Generate a Sign in with Apple button with center-aligned text.
- [Get a Sign in with Apple button that contains just the Apple logo.](./get-a-sign-in-with-apple-button-that-contains-just-the-apple-logo.md)
  Generate a Sign in with Apple button image containing just the Apple logo.


---

*[View on Apple Developer](https://developer.apple.com/documentation/signinwithapplerestapi/get-a-sign-in-with-apple-button-that-is-left-aligned.)*