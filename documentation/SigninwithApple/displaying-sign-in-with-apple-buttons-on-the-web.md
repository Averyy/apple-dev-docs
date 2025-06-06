# Displaying Sign in with Apple buttons on the web

**Framework**: Sign in with Apple

Configure the appearance of Sign in with Apple buttons with CSS styles.

#### Overview

You can specify the display of your Sign in with Apple button, and edit its appearance and size to fit your webpage. For a description of the button types and usage information, see [`Sign in with Apple Buttons`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/sign-in-with-apple/overview/#sign-in-with-apple-buttons) in the Human Interface Guidelines.

![An image that shows a Sign in with Apple Button 140 points wide with white text on a black background, a Sign in with Apple button 30 points high with black text on a white background, and a Sign in with Apple logo-only button with a 1:1 aspect ratio.](https://docs-assets.developer.apple.com/published/28d981b3f2c813fc757f128425d8d698/media-3703091%402x.png)

##### Create a Wrapper Tag and Configure Localization

Start by creating a wrapper tag for your button. Set the `id` to “`appleid-signin`”.

```javascript
<div id="appleid-signin"></div>
```

To configure the localization of the Sign in with Apple button, embed your desired localization code within the URI below:

```javascript
<script type="text/javascript" src="https://appleid.cdn-apple.com/appleauth/static/jsapi/appleid/1/en_US/appleid.auth.js"></script>
```

Replace `en_US` in the code above with your localization code. For a list of available locales, see [`Incorporating Sign in with Apple into other platforms`](incorporating-sign-in-with-apple-into-other-platforms.md).

##### Specify Property Values

The folowing example creates a black Sign in with Apple button.

```javascript
<html>
    <head>
        <meta name="appleid-signin-client-id" content="[CLIENT_ID]">
        <meta name="appleid-signin-scope" content="[SCOPES]">
        <meta name="appleid-signin-redirect-uri" content="[REDIRECT_URI]">
        <meta name="appleid-signin-state" content="[STATE]">
    </head>
    <style>
        .signin-button {
            width: 210px;
            height: 40px;
        }
    </style>
    <body>
        <div id="appleid-signin" class="signin-button" data-color="black" data-border="true" data-type="sign-in"></div>
        <script type="text/javascript" src="https://appleid.cdn-apple.com/appleauth/static/jsapi/appleid/1/en_US/appleid.auth.js"></script>
    </body>
</html>
```

Control the size of the button by adding a class that contains the desired CSS `width` and `height` styles. The above example creates a button that’s 210 pixels wide and 40 pixels high, and sets the properties of the Sign in with Apple button as described in the following sections.

###### Set the Mode

To configure the appearance of the Sign in with Apple button, set the `data-mode` property to one of the following values:

###### Set the Type

You can request a specific button type by setting the `data-type` property of the Sign in with Apple button to one of the following values:

###### Set the Color

To configure the background color of the Sign in with Apple button, set the `data-color` property to one of the following values:

###### Set the Border and Radius

To configure the border of the Sign in with Apple button, set the `data-border` property to one of the following values:

To configure the border radius of the button, set the `data-border-radius` property to a number between `0—50`. The default is `15`.

###### Set the Width and Height

To configure the width of the Sign in with Apple button, set the `data-width` property to a value in points between `130—375`, or `100%` to fit the container size. The default is `100%`.

To configure the height of the button, set the `data-height` property to a value in points between `30—64`, or `100%` to fit the container size. The default is `100%`.

###### Set the Logo Size and Position

You can control the size and position of the Apple logo on the Sign in with Apple button. These settings only work if you set `data-mode` to `left-align`.

To configure the logo size on the button, set the `data-logo-size` property to one of the following values:

To configure the logo position on the button, set the `data-logo-position` property to a number in points. The minimum value is `0` and the maximum is the label position. The logo remains positioned to the left of the label. The system may override the value to maintain proper margins for the logo and font size.

###### Set the Label Position

You can configure the position of the text in the Sign in with Apple button if you set `data-mode` to `left-align`. Set the `data-label-position` property to a value in points between `0` and half the width of the button. The default is `0`.

## See Also

- [Configuring your environment for Sign in with Apple](configuring-your-environment-for-sign-in-with-apple.md)
  Authenticate users with your web service by associating an existing app with a Services ID and private key.
- [Processing changes for Sign in with Apple accounts](processing-changes-for-sign-in-with-apple-accounts.md)
  Manage user-initiated modifications to maintain privacy with server-to-server notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/signinwithapple/displaying-sign-in-with-apple-buttons-on-the-web)*