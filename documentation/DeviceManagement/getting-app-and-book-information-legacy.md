# Getting App and Book Information (Legacy)

**Framework**: Device Management

Use a web service to find details about apps and books to show to your users.

#### Overview

To provide users with metadata for the apps and books that they’re managing, such as artwork, the `contentMetadataLookup` url in the [`Service Config`](service-config.md) response allows an MDM server to query the store for app and book metadata.

##### Perform a Lookup

The URL query string tells the content metadata lookup service which app or book to look up. You must use a `GET` HTTP method for this request.

The platform filters the content, and the useful values for the `platform` query parameter are:

```None
- term `enterprisestore`: For apps in the enterprise store
- term `volumestore`: For apps in the educational store
```

For example, to get B2B app content, append `platform`=`enterprisestore` to your query string.

The following is an example of the URL to look up an app:

`https://uclient-api.itunes.apple.com/WebObjects/MZStorePlatform.woa/wa/lookup?version=2&id=361309726&p=mdm-lockup&caller=MDM&platform=enterprisestore&cc=us&l=en`

A typical response looks like the following:

```javascript
{
  "results": {
    "361309726": {
      "artwork": [
        {
          "width": 128,
          "height": 128,
          "url": "https://is4-ssl.mzstatic.com/image/thumb/Purple113/v4/73/d4/73/73d47332-fefc-d350-2984-5b4a4755a502/AppIcon-0-1x_U007emarketing-0-0-GLES2_U002c0-512MB-sRGB-0-0-0-85-220-0-0-0-6.png/128x128bb.png"
        },
        {
          "width": 216,
          "height": 216,
          "url": "https://is4-ssl.mzstatic.com/image/thumb/Purple113/v4/73/d4/73/73d47332-fefc-d350-2984-5b4a4755a502/AppIcon-0-1x_U007emarketing-0-0-GLES2_U002c0-512MB-sRGB-0-0-0-85-220-0-0-0-6.png/360x216bb.png"
        }
      ],
      "artistName": "Apple",
      "hasMessagesExtension": false,
      "url": "https://itunes.apple.com/us/app/pages/id361309726?mt=8",
      "shortUrl": "https://itunes.apple.com/us/app/pages/id361309726?mt=8",
      "softwareInfo": {
        "seller": "Apple Inc.",
        "languagesDisplayString": "English, Arabic, Catalan, Chinese (Hong Kong), Croatian, Czech, Danish, Dutch, Finnish, French, German, Greek, Hebrew, Hindi, Hungarian, Indonesian, Italian, Japanese, Korean, Malay, Norwegian, Polish, Portuguese, Romanian, Russian, Simplified Chinese, Slovak, Spanish, Swedish, Thai, Traditional Chinese, Turkish, Ukrainian, Vietnamese",
        "requirementsString": "Requires iOS 11.0 or later. Compatible with iPhone, iPad, and iPod touch.",
        "eulaUrl": "https://itunes.apple.com/WebObjects/MZStore.woa/wa/viewEula?cc=us&id=361309726",
        "supportUrl": "http://www.apple.com/support/ipad/pages/",
        "websiteUrl": "http://www.apple.com/pages/",
        "privacyPolicyUrl": "https://www.apple.com/legal/privacy/en-ww",
        "privacyPolicyTextUrl": null
      },
      "ageBand": null,
      "isFirstParty": false,
      "deviceFamilies": [
        "iphone",
        "ipad",
        "ipod"
      ],
      "genreNames": [
        "Productivity",
        "Business"
      ],
      "whatsNew": "This update contains stability and performance improvements.",
      "isPreorder": false,
      "nameSortValue": "Pages",
      "id": 361309726,
      "releaseDate": "2010-04-01",
      "userRating": {
        "value": 3.5,
        "ratingCount": 37414,
        "valueCurrentVersion": 3.5,
        "ratingCountCurrentVersion": 10523
      },
      "editorialBadgeInfo": null,
      "contentRatingsBySystem": {
        "appsApple": {
          "name": "4+",
          "value": 100,
          "rank": 1
        }
      },
      "name": "Pages",
      "uber": null,
      "artistUrl": "https://itunes.apple.com/us/developer/apple/id284417353?mt=8",
      "ovalArtwork": null,
      "nameRaw": "Pages",
      "subtitle": "Documents that stand apart",
      "bundleId": "com.apple.Pages",
      "isFirstPartyHideableApp": false,
      "isVppDeviceBasedLicensingEnabled": true,
      "hasInAppPurchases": false,
      "isAppleWatchSupported": false,
      "isB2BCustomApp": false,
      "kind": "iosSoftware",
      "circularArtwork": null,
      "copyright": "© 2010 - 2019 Apple Inc.",
      "latestVersionReleaseDate": "Apr 9, 2019",
      "requiresGameController": false,
      "isHiddenFromSpringboard": false,
      "artistId": 284417353,
      "genres": [
        {
          "genreId": "6007",
          "name": "Productivity",
          "url": "https://itunes.apple.com/us/genre/id6007",
          "mediaType": "8"
        },
        {
          "genreId": "6000",
          "name": "Business",
          "url": "https://itunes.apple.com/us/genre/id6000",
          "mediaType": "8"
        }
      ],
      "minimumOSVersion": "11.0",
      "isGameControllerSupported": false,
      "is32bitOnly": false,
      "isSiriSupported": false,
      "description": {
        "standard": "Pages is the most beautiful word processor you've ever seen on a mobile device.  Start with an Apple-designed template to instantly create gorgeous reports, digital books, resumes, posters and more. Or use a blank document and create your own design. Easily add images, movies, audio, charts and shapes. You can even draw and annotate using Apple Pencil on supported devices, or your finger. Pages has been designed exclusively for the iPad, iPhone, and iPod touch.\n\nWith iCloud built in, your documents are kept up to date across all your devices. And with real-time collaboration, your team will be able to work together at the same time on a Mac, iPad, iPhone, or iPod touch — even on a PC.\n\nDraw and annotate using Apple Pencil, or your finger\n• Easily add drawings with pen, pencil, crayon, and fill tools. Then animate them and watch them come to life\n• Use Smart Annotation Beta to add comments and marks that stay anchored to their associated text\n\nCollaborate with others at the same time\n• With real-time collaboration, your whole team can work together on a document at the same time\n• Collaboration is built right in to Pages on the Mac, iPad, iPhone and iPod touch. PC users can collaborate too \n• Share your document publicly or with specific people\n• You can easily see who's currently in the document with you\n• View other people's cursors to follow their edits\n• Available on documents stored in iCloud or in Box\n\nGet started quickly\n• Choose from over 70 Apple-designed templates to instantly create beautiful reports, digital books, resumes, cards, posters and more\n• Import and edit Microsoft Word and text files\n\nCreate beautiful documents\n• Format your document with gorgeous styles, fonts, and textures\n• Type vertically in your entire document or in an individual text box\n• Enhance your document with a library of over 700 editable shapes\n• Easily add images, video, and audio\n• Add an image gallery to view a collection of photos on the same page\n• Create interactive EPUB books that can be shared with others or published to Apple Books for download or purchase\n\nAdvanced tools\n• Use the table of contents view to easily navigate your document or book\n• Add comments and join threaded conversations\n• Turn on change tracking to mark up a document as you edit it\n• Add bookmarks to easily link from one part of your document to another\n• View pages side by side as you work\n• Turn on facing pages to format your document as two-page spreads \n• Add linked text boxes so text easily flows from one place to another\n• Create footnotes and endnotes and view word counts\n• Add elegant mathematical equations using LaTeX or MathML notation\n• Quickly open password-protected documents using Touch ID or Face ID on supported devices\n• Use presenter mode to easily read and auto scroll text while giving a speech\n\niCloud\n• Turn on iCloud so your documents are automatically available on your Mac, iPad, iPhone, iPod touch, and iCloud.com\n• Access and edit your documents from a Mac or PC browser at www.icloud.com with Pages for iCloud\n\nShare a copy of your work\n• Use AirDrop to send your document to anyone nearby\n• Quickly and easily share a link to your work via Mail, Messages, Twitter, or Facebook \n• Export your document in EPUB, Microsoft Word, and PDF format\n• Print wirelessly with AirPrint, including page range selection, number of copies, and two-sided printing\n\nSome features may require Internet access; additional fees and terms may apply."
      },
      "requiredCapabilities": "arm64 ",
      "offers": [
        {
          "actionText": {
            "short": "Get",
            "medium": "Get",
            "long": "Get App",
            "downloaded": "Installed",
            "downloading": "Installing"
          },
          "type": "get",
          "priceFormatted": "$0.00",
          "price": 0,
          "buyParams": "productType=C&price=0&salableAdamId=361309726&pricingParameters=STDQ&pg=default&marketType=ENT&appExtVrsId=830786363",
          "version": {
            "display": "5.0.1",
            "externalId": 830786363
          },
          "assets": [
            {
              "flavor": "iosSoftware",
              "size": 549427200
            }
          ]
        }
      ],
      "contentRating": {
        "system": "GAMES",
        "name": "4+",
        "value": 100,
        "rank": 1
      }
    }
  },
  "version": 1,
  "isAuthenticated": false,
  "meta": {
    "storefront": {
      "id": "143441",
      "cc": "US"
    },
    "language": {
      "tag": "en-us"
    }
  }
}
```

##### Authenticate for Custom Apps

If the MDM client includes the organization’s `sToken` in the request as a cookie, an MDM server can get authenticated app metadata for B2B apps that the organization owns, as well as apps that users can still redownload, but no longer purchase.

You must include the organization’s `sToken` as a cookie named `itvt` to access the authenticated metadata.

The following is an example of the request with the added cookie:

```javascript
curl --location --request GET 'https://uclient-api.itunes.apple.com/WebObjects/MZStorePlatform.woa/wa/lookup?version=2&id=451796775&p=mdm-lockup&caller=MDM&platform=enterprisestore&cc=us&l=en' \
 --cookie "itvt={sToken}"
```

A typical response looks like the following:

```javascript
{
    "isAuthenticated": false,
    "meta": {
        "language": {
            "tag": "en-us"
        },
        "storefront": {
            "cc": "US",
            "id": "143441"
        }
    },
    "results": {
        "451796775": {
            "artistId": "395961493",
            "artistName": "GamekitTester",
            "artistUrl": "https://apps.apple.com/us/developer/gamekittester/id395961493",
            "artwork": {
                "bgColor": "abd763",
                "hasAlpha": false,
                "hasP3": false,
                "height": 1024,
                "supportsLayeredImage": false,
                "textColor1": "000000",
                "textColor2": "1c190d",
                "textColor3": "222b13",
                "textColor4": "383f1e",
                "url": "https://is2-ssl.mzstatic.com/image/thumb/Purple124/v4/f3/2c/7f/f32c7f07-0441-052d-dc71-a406c9f90c09/AppIcon-0-1x_U007emarketing-0-0-GLES2_U002c0-512MB-sRGB-0-0-0-85-220-0-0-0-7.png/{w}x{h}bb.{f}",
                "width": 1024
            },
            "bundleId": "com.apple.b2bTest2",
            "contentRatingsBySystem": {
                "appsApple": {
                    "name": "4+",
                    "rank": 1,
                    "value": 100
                }
            },
            "copyright": "\u00a9 2011",
            "description": {
                "standard": "B2B App Store Testing App"
            },
            "deviceFamilies": [
                "iphone",
                "ipad",
                "ipod"
            ],
            "editorialArtwork": {},
            "genreNames": [
                "Utilities"
            ],
            "genres": [
                {
                    "genreId": "6002",
                    "mediaType": "8",
                    "name": "Utilities",
                    "url": "https://itunes.apple.com/us/genre/id6002"
                }
            ],
            "id": "451796775",
            "isB2BCustomApp": true,
            "isVppDeviceBasedLicensingEnabled": true,
            "kind": "iosSoftware",
            "latestVersionReleaseDate": "Dec 19, 2018",
            "minimumOSVersion": "12.1",
            "name": "b2b Test 2",
            "nameRaw": "b2b Test 2",
            "nameSortValue": "bbTest",
            "watchBundleId": "com.example.bbTest.watchkitapp",
            "offers": [
                {
                    "actionText": {
                        "downloaded": "Installed",
                        "downloading": "Installing",
                        "long": "Get App",
                        "medium": "Get",
                        "short": "Get"
                    },
                    "assets": [
                        {
                            "flavor": "iosSoftware",
                            "size": 882688
                        }
                    ],
                    "buyParams": "productType=C&price=0&salableAdamId=451796775&pricingParameters=STDQ&pg=default&marketType=ENT&appExtVrsId=126462631",
                    "price": 0,
                    "priceFormatted": "$0.00",
                    "type": "get",
                    "version": {
                        "display": "3.0",
                        "externalId": 126462631
                    }
                }
            ],
            "releaseDate": "2018-12-19",
            "requiredCapabilities": "arm64 ",
            "shortUrl": "https://apps.apple.com/us/app/b2b-test-2/id451796775",
            "softwareInfo": {
                "eulaUrl": null,
                "isGameCenter": true,
                "languagesDisplayString": "English",
                "privacyPolicyTextUrl": null,
                "privacyPolicyUrl": "http://apple.com/privacy",
                "requirementsString": "Requires iOS\u00a012.1 or later. Compatible with iPhone, iPad, and iPod\u00a0touch.",
                "seller": "Apple Inc. - Gamekit Tester",
                "supportUrl": "http://support.apple.com",
                "websiteUrl": null
            },
            "url": "https://apps.apple.com/us/app/b2b-test-2/id451796775",
            "userRating": {
                "ratingCount": 0,
                "ratingCountCurrentVersion": 0,
                "value": 0,
                "valueCurrentVersion": 0
            },
            "whatsNew": "lksdjfsdljfdsljfs"
        }
    },
    "version": 2
}
```

The `isAuthenticated` field is always `false`. To verify proper authentication, check the `results` field for content. An empty `results` set means one of the following:

- The user doesn’t have access to the queried app or book.
- The provided `id` isn’t valid.
- Authentication failed.

The `watchBundleID` key indicates that the app runs on Apple Watch. The value is the watch’s bundle identifier, which can differ from the main bundle identifier that the iPhone it’s paired with uses.

When the `results` set is empty, a typical response looks like the following:

```javascript
{
    "isAuthenticated": false,
    "meta": {
        "language": {
            "tag": "en-us"
        },
        "storefront": {
            "cc": "US",
            "id": "143441"
        }
    },
    "results": {},
    "version": 2
}
```

##### Identify Universal Apps

When an MDM client queries the store for an app, it may need to determine whether the app is universal so it can assess what devices it can assign the app to.

To make this determination, an MDM client looks for the following two fields:

```None
- term `deviceFamilies`: Supported device families
- term `kind`: Type of content
```

A universal app lists `mac` in `deviceFamilies` and has `kind` equal to `iosSoftware`.

Use `platform=macappstore` in your query string to retrieve Mac specific metadata when using `contentMetadataLookup.`

By default, using `platform=enterprisestore` or `platform=volumestore` returns iOS metadata for an app designed for iPad on a Mac with M1 or M2.

The following is an example of a typical response from an app designed for iPad on a Mac with M1 or M2:

```javascript
{
    "results": {
        "640199958": {
            ...
            "deviceFamilies": [
                "mac",.
                "tvos",
                "iphone",
                "ipad",
                "ipod"            
            ],
            ...
            "kind": "iosSoftware",
            ...
        }
    },
    "version": 1,
    "isAuthenticated": false,
    "meta": {
        "storefront": {
            "id": "143441",
            "cc": "US"
        },
        "language": {
            "tag": "en-us"
        }
    }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/getting-app-and-book-information-legacy)*